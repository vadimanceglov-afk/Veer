from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm, CustomUserCreationForm

def user_logout(request):
    logout(request)
    return redirect("main_page")

def user_login(request):
    if request.method == "GET":
        form = LoginForm()

    elif request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main_page")


    return render(request, template_name="auth_sistem/login.html", context={"form": form})


def user_register(request):    
    if request.method == "GET":
        form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("main_page")

    return render(request, template_name="auth_sistem/register.html", context={"form": form})