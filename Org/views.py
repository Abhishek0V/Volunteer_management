# org/views.py
from django.shortcuts import render, redirect
from .forms import OrgSignupForm

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
