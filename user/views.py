from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserForm
from django.views.generic import View
from django.views.generic.edit import CreateView
from django_datatables_view.base_datatable_view import BaseDatatableView

class UserView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'user/index.html')
    
    def post(self, request, *args, **kwargs):
        pass

class UserBaseDatatableView(BaseDatatableView):
    model = User
    columns = ['id', 'name', 'email', 'created_at']
    max_display_length = 10
    
class UserCreateView(CreateView):
    def form_valid(self, request, *args, **kwargs):
        pass
     
    model = User
    columns = ['id', 'name', 'email', 'created_at']
    max_display_length = 10


@login_required
def index(request):
    if request.method == 'GET':
        users = User.objects.all();
        return render(request, 'user/index.html', {'users': users})

@login_required    
def create(request):    
    form = UserForm(request.POST or None, request.FILES or None)
    if request.method == 'GET':
        return render(request, 'user/create.html', {'form': form})
    elif request.method == 'POST':
        print(form.is_valid())
        return HttpResponse("Okay")
        # if form.is_valid:
        #     form.save()
        #     return redirect('/user/')

@login_required
def update(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=user)
    
    if form.is_valid():
        form.save()
        return redirect('/user/')
    
    return render(request, 'user/update.html', {'form': form})

@login_required
def delete(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=user)
    
    if request.method == 'POST':
        user.delete()
        return redirect('/user/')
    
    return render(request, 'user/delete.html', {'form': form})