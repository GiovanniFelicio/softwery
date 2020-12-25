from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserForm

@login_required
def index(request):
    if request.method == 'GET':
        users = User.objects.all();
        return render(request, 'userIndex.html', {'users': users})

@login_required    
def create(request):    
    form = UserForm(request.POST or None, request.FILES or None)
    if request.method == 'GET':
        return render(request, 'userCreate.html', {'form': form})
    elif request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('/user/')

@login_required
def update(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=user)
    
    if form.is_valid():
        form.save()
        return redirect('/user/')
    
    return render(request, 'userUpdate.html', {'form': form})

@login_required
def delete(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=user)
    
    if request.method == 'POST':
        user.delete()
        return redirect('/user/')
    
    return render(request, 'userDelete.html', {'form': form})