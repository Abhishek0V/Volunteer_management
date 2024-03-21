from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import VolSignupForm
from django.contrib import messages
from django.contrib.auth.models import User  # Import Django's built-in User model

def profile(request):
    return render(request, 'profile.html')

def volunteer_login(request):
    error_message = None
    form = AuthenticationForm()  # Instantiate AuthenticationForm

    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        print("Email:", email)
        print("Password:", password)
        user = authenticate(request, email=email, password=password)
        print("Request:", request)
        print("User:", user)
        if user is not None:
            login(request, user)  # Use login function to log in the user
            print("User is logged in")
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    else:
        print("Email or password is missing in the form data.")

    return render(request, 'log.html')

# signUp -----------------

def vol_signup(request):
    if request.method == 'POST':
        form = VolSignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Form is saved")  # Redirect to a success page or login page
            return redirect('home')  # Adjust this to your actual login URL
    else:
        form = VolSignupForm()
    return render(request, 'signup.html', {'form': form})


def volunteer_logout(request):
    logout(request)  # Log out the user
    return redirect('home')