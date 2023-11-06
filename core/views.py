from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

def home(request):
    return render(request, 'home.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username!!')
            return redirect('/login/')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid/Incorrect Username or Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('/')

def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, 'This username is already exist')
            return redirect('/signup/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        messages.info(request, 'Account created Successfulyy!!')
        return redirect('/login/')

    return render(request, 'register.html')

def videoCall(request):
    return render(request, 'call.html')

def joinRoom(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/new-meeting?roomID=" + roomID)
    return render(request, 'join.html')