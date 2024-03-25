# events/forms.py
from django import forms
from .models import Events,Gallery

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['Event_Name', 'Event_Description', 'Location', 'Event_Date', 'Number_of_Volunteer', 'Size_of_Event', 'poster', 'Registration_option']

class OrgImageForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['img']