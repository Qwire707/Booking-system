from django.shortcuts import render
from .forms import UserRegistrationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == "POST":
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect("login")
        else:
            messages.error(request, "Дані введені некоректно!")
            return redirect("login")
    else:
        register_form = UserRegistrationForm()
        return render(request, "register.html", context={"register_form": register_form})

def login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(request, username=username,
            password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Дані введені некоректно!")
                return redirect("login")
        else:
            messages.error(request, "Дані введені некоректно!")
            return redirect("login")
    else:
        login_form = AuthenticationForm()
        return render(request, "login.html", context={"login_form":login_form})

def logout_view(request):
    logout(request)
    return redirect('login')

