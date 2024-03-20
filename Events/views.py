from django.shortcuts import get_object_or_404, redirect, render
from .models import Events
from .forms import EventForm

# Create your views here.

def home(request):
    events = Events.objects.all()
    context = { 'events': events}
    return render(request, 'hom.html', context)

def events(request, pk):
    event = get_object_or_404(Events, Event_ID=pk)
    context = {'event': event}
    return render(request, 'events.html', context)

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful form submission
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})