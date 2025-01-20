from django.shortcuts import get_object_or_404, render, redirect
from .forms import SignupForm, LoginForm
from django.contrib import messages 
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm 
from django.contrib.auth import login, authenticate, logout,update_session_auth_hash

def Home(request):
    return render(request, 'index.html') 

def SignupPage(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Signup successful! Welcome, {user.username}.')
            return redirect('login')
        else:
            messages.error(request, 'Signup failed. Please correct the errors below.')
    else: 
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form}) 


def LoginPage(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) 
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('profile')  
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please fill out form correctly.")
    else:
        form = LoginForm()  
    
    return render(request, 'login.html', {'form': form})


def LogoutPage(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')


def ProfilePage(request):
    return render(request, 'profile.html') 

def Changepasswithprev(request):
    if request.method  ==  'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "You have successfully changed password.")
            return redirect('profile')
        else:
            messages.error(request, "Please fill out form correctly.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepasswithprev.html', {'form': form}) 

def Changepasswithoutprev(request):
    if request.method  ==  'POST':
        form = SetPasswordForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "You have successfully changed password.")
            return redirect('profile')
        else:
            messages.error(request, "Please fill out form correctly.")
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'changepasswithprev.html', {'form': form}) 
