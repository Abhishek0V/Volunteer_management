# forms.py

from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", name="email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    class Meta:
        fields = ['email', 'password']
        labels = {
            'email': 'Email',
            'password': 'Password'
        }
        widgets = {
            'password': forms.PasswordInput()
        }