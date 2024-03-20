from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User  # Import Django's built-in User model

def profile(request):
    return render(request, 'profile.html')

def volunteer_login(request):
    error_message = None
    form = AuthenticationForm()  # Instantiate AuthenticationForm

    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        print("Email:", email)
        print("Password:", password)
        
        if email and password:
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

    return render(request, 'login.html', {'form': form, 'error_message': error_message})
