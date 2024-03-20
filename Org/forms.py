# org/forms.py
from django import forms
from .models import Org
from User.models import User

class OrgSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Org
        fields = ['Org_Name', 'Location', 'verified', 'profile']

    def __init__(self, *args, **kwargs):
        super(OrgSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField()
        self.fields['Role'] = forms.ChoiceField(choices=User.user_type)

    def save(self, commit=True):
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            Role=self.cleaned_data['Role'],
            password=self.cleaned_data['password']
        )
        org = super(OrgSignupForm, self).save(commit=False)
        org.user = user
        if commit:
            org.save()
        return org
