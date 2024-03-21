# views.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from Volunteer.models import Notification, volunteer
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

def registered_volunteers(request, event_id):
    event = Events.objects.get(Event_ID=event_id)
    registered_volunteers = Registered_volunteers.objects.filter(Event=event)
    
    if request.method == 'POST':
        selected_volunteers = request.POST.getlist('selected_volunteers[]')
        for volunteer_id in selected_volunteers:
            volunteer = Registered_volunteers.objects.get(pk=volunteer_id)
            volunteer.Selected = True
            volunteer.save()
        return redirect('registered_volunteers', event_id=event_id)

    return render(request, 'registered_volunteers.html', {'event': event, 'registered_volunteers': registered_volunteers})

def selected_volunteers(request, event_id):
    event = Events.objects.get(Event_ID=event_id)
    selected_volunteers = Registered_volunteers.objects.filter(Event=event, Selected=True)
    return render(request, 'selected_volunteers.html', {'event': event, 'selected_volunteers': selected_volunteers})

def send_notification(request, event_id):
    if request.method == 'POST':
        notification_text = request.POST.get('notification_text')

        event = Events.objects.get(Event_ID=event_id)

        for registered_volunteer in Registered_volunteers.objects.filter(Event=event, Selected=True):
            volunteer_instance = registered_volunteer.Volunteers
            # Check if a notification already exists for this volunteer
            existing_notification = Notification.objects.filter(vol=volunteer_instance).exists()
            if not existing_notification:
                Notification.objects.create(vol=volunteer_instance, text=notification_text)

        return redirect('selected_volunteers', event_id=event_id)
    else:
        return render(request, 'selected_volunteers.html', {'event_id': event_id})
    
def get_notifications(request):
    if request.user.is_authenticated and hasattr(request.user, 'vol_profile'):
        volunteer = request.user.vol_profile
        notifications = Notification.objects.filter(vol=volunteer)
        data = [{'text': notification.text} for notification in notifications]
        return JsonResponse(data, safe=False)
    return JsonResponse([], safe=False)  # Return empty list if user is not logged in or not a volunteer