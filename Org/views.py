# org/views.py
from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import OrgSignupForm
from django.contrib.auth.decorators import login_required

def org_signup(request):
    if request.method == 'POST':
        form = OrgSignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Form is saved")
            # Redirect to a success page or login page
            return redirect('home')  # Adjust this to your actual login URL
    else:
        form = OrgSignupForm()
    return render(request, 'signup.html', {'form': form})

def org_login(request):
    error_message = None
    form = AuthenticationError()  # Instantiate AuthenticationForm

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
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    else:
        print("Email or password is missing in the form data.")

    return render(request, 'org-login.html')

@login_required
def dashboard(request):
    # Retrieve the logged-in organization
    organization = request.user.org_profile

    # Retrieve events associated with the logged-in organization
    events = organization.conducting_Org.all()

    # Render the dashboard template with events passed in the context
    return render(request, 'dashboard.html', {'events': events})