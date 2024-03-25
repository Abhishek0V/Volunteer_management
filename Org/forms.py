from django import forms
from .models import Org
from User.models import User

class OrgSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Org
        fields = ['Org_Name', 'Location', 'profile']

    def save(self, commit=True):
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            Role='Org',  # Set role to organization
            password=self.cleaned_data['password']
        )
        org = super(OrgSignupForm, self).save(commit=False)
        org.user = user
        org.verified = True  # Set verified to True
        if commit:
            org.save()
        return org

    def __init__(self, *args, **kwargs):
        super(OrgSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField()