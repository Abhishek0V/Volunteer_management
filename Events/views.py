# views.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect

from Volunteer.models import volunteer
from .models import Events, Registered_volunteers
from .forms import EventForm


def home(request):
    events = Events.objects.all()
    context = { 'events': events}
    return render(request, 'home.html', context)

def events(request, pk):
    event = get_object_or_404(Events, Event_ID=pk)
    context = {'event': event}
    return render(request, 'events.html', context)

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            # Check if the user is an organization
            if request.user.Role == 'Org' and hasattr(request.user, 'org_profile'):
                org = request.user.org_profile
                event.Created_Org_id = org.Org_ID
                event.save()
                return redirect('home')
            else:
                # If the user is not an organization or doesn't have an associated organization,
                # handle the error or redirect as needed
                return HttpResponse("You are not authorized to create an event.")
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

@login_required
def register_for_event(request, event_id):
    event = Events.objects.get(pk=event_id)
    
    # Check if the user is a volunteer
    if request.user.Role != 'Vol':
        return HttpResponseForbidden("Only volunteers can register for events.")
    
    # Retrieve the volunteer instance associated with the logged-in user
    try:
        volunteer_instance = volunteer.objects.get(user=request.user)
    except volunteer.DoesNotExist:
        # Handle case where volunteer instance doesn't exist for the user
        # Redirect or display an error message as appropriate
        pass
    
    # Assuming the user is a volunteer and a volunteer instance exists, proceed with registration
    Registered_volunteers.objects.create(Event=event, Volunteers=volunteer_instance)
    return redirect('home')