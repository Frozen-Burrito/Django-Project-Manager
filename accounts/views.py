from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import UserSignupForm, AccountEditForm

# Create your views here.

def user_profile(request):

    account = request.user.account
    context = { 'account': account } 
    return render(request, 'profile.html', context)

def user_profile_edit(request):

    account = request.user.account
    form = AccountEditForm( instance=account )

    if request.method == 'POST':
        form = AccountEditForm( request.POST, request.FILES, instance=account )

        if form.is_valid():
            form.save()
            return redirect('accounts:profile')

    context = { 'account': account, 'form': form}

    return render(request, 'profile_edit.html', context)

def login_page(request):

    context = {} 

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else: 
            messages.info(request, 'Incorrect username or password')
            return render(request, 'login.html', context)

        
    return render(request, 'login.html', context)

def signup_page(request):

    form = UserSignupForm()

    if request.method == 'POST':
        form = UserSignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account for ' + username + ' was created successfully')
            return redirect('/projects/dashboard')

    context = { 'form': form } 

    return render(request, 'signup.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home') 