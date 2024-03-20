# In forms.py
from django import forms
from .models import Org

class OrgRegistrationForm(forms.ModelForm):
    class Meta:
        model = Org
        fields = ['Org_Name','profile','Location']  
