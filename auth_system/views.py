from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate

def user_logout(request):
    logout(request)
    return redirect("main_page")