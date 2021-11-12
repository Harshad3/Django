from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login.html')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request,'Email Already exists')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'Username is taken')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            user.save()
            print('User Created')
            return redirect('login')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
