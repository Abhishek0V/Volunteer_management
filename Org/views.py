from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import OrgSignupForm
from django.contrib.auth.decorators import login_required

def org_signup(request):
    if request.method == 'POST':
        form = OrgSignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Organization signed up successfully.')
            return redirect('home')  # Redirect to a success page or login page
    else:
        form = OrgSignupForm()
    return render(request, 'signup.html', {'form': form})

def org_login(request):
    error_message = None
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None and user.Role == 'Org':
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid credentials or user is not an organization.'
    return render(request, 'org-login.html', {'error_message': error_message})

@login_required
def dashboard(request):
    # Retrieve the logged-in organization
    organization = request.user.org_profile

    # Retrieve events associated with the logged-in organization
    events = organization.conducting_Org.all()

    # Render the dashboard template with events passed in the context
    return render(request, 'dashboard.html', {'events': events})