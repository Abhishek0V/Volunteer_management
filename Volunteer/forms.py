# forms.py
from .models import volunteer
from User.models import User
from django import forms

# class LoginForm(forms.Form):
#     email = forms.EmailField(label="Email", name="email")
#     password = forms.CharField(label="Password", widget=forms.PasswordInput)
#     class Meta:
#         fields = ['email', 'password']
#         labels = {
#             'email': 'Email',
#             'password': 'Password'
#         }
#         widgets = {
#             'password': forms.PasswordInput()
#         }

class VolSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = volunteer
        fields = ['Name','Age','Gender','Location','profile_img']

    def __init__(self, *args, **kwargs):
        super(VolSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField()
        

    def save(self, commit=True):
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            Role='Vol',
            password=self.cleaned_data['password']
        )
        org = super(VolSignupForm, self).save(commit=False)
        org.user = user
        if commit:
            org.save()
        return org

