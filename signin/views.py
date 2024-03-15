from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse

def signin(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            next_param = request.POST.get('next')
            if next_param:
                url = next_param
            else:
                url = reverse('home')
            return redirect(url)
        else:
            messages.error(request, 'Email or Password incorrect')

    return render(request, 'signin.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        if first_name == "":
            messages.error(request, "You must enter Fisrt Name")
            return render(request, 'signup.html')
        last_name = request.POST['last_name']
        if last_name == "":
            messages.error(request, "You must enter Last Name")
            return render(request, 'signup.html')
        username = request.POST['username']
        if username == "":
            messages.error(request, "You must enter Username")
            return render(request, 'signup.html')
        email = request.POST['email']
        if email == "":
            messages.error(request, "You must enter Email")
            return render(request, 'signup.html')
        password = request.POST['password']
        if password == "":
            messages.error(request, "You must enter Password")
            return render(request, 'signup.html')
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")

            else:
                user = User.objects.create_user(
                        first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                user.save()
                login(request, user)
                next_param = request.POST.get('next')
                if next_param:
                    url = next_param
                else:
                    url = reverse('home')
                return redirect(url)


        else:
            messages.error(request, 'Password not matched')

    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect("/")