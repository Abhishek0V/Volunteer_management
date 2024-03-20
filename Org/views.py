from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from .forms import OrgRegistrationForm

def org_registration(request):
    if request.method == 'POST':
        form = OrgRegistrationForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new Org object
            org = form.save(commit=False)
            # Assign the current user to the 'user' field
            org.user = request.user
            # Save the object
            org.save()
            print("org created")
            # Redirect to a success page or any other desired page
            return redirect('home')
    else:
        # Display the form for GET requests
        form = OrgRegistrationForm()
    
    return render(request, 'org-signup.html', {'form': form})