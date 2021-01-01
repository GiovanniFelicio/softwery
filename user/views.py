from django.http import HttpResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserForm
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views import View

class UserCreateView(View):
    def get(self, request):
        return render(request, 'user/create.html')
    
    def post(self, request):
        pass


class UserBaseDatatableView(BaseDatatableView):
    model = User
    columns = ['id', 'name', 'email', 'createdAt']
    max_display_length = 10
    
    def get_filter_method(self):            
        return 'icontains'


@login_required
def index(request):
    if request.method == 'GET':
        return render(request, 'user/index.html')

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

@login_required
def find(request):
    if request.method == 'GET':
        data = request.GET
        value = data['value']
        field = data['field']
        
        user = User.objects.raw("SELECT id FROM SFT_USER WHERE %s = '%s'" %(field, value))
        
        if user is not None and len(user) > 0:
            return HttpResponse(status=409)
        
    return HttpResponse("ok")