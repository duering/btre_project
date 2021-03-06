from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Register user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # Check if passwords match
        if password != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        # Check username
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'That username already exists')
            return redirect('register')
        # Check email
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'That email already exists')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password,
             email=email, first_name=first_name, last_name=last_name)
            # Login after register
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('index')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        # Login user
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out')
        return redirect('index')

def dashboard(request):
    user_contacts = Contact.objects.filter(user_id=request.user.id).order_by('contact_date')
    return render(request, 'accounts/dashboard.html', {
        'contacts': user_contacts
    })