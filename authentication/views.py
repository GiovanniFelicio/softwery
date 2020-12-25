from django.shortcuts import render, redirect
from django.contrib.auth import logout

def doLogout(request):
    logout(request)
    return redirect('indexHome')
