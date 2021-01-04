from django.http import HttpResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserForm
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views import View
from .helper import UserHelper
from softwery.utils import formUtil
from django.contrib import messages

from user.models import User
from rest_framework import viewsets
from rest_framework import permissions, authentication
from user.serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


@login_required
def find(request):
    if request.method == 'GET':
        data = request.GET
        value = data['value']
        field = data['field']
        
        user = UserHelper.find_by_field_and_value(field, value)
        
        if user is not None and len(user) > 0:
            return HttpResponse(status=409)
        
    return HttpResponse(status=200)

class UserIndexView(View):
    def get(self, request):
        return render(request, 'user/index.html')
    
    def post(self, request):
        pass
    
class UserCreateView(View):
    def get(self, request):
        return render(request, 'user/create.html')
    
    def post(self, request):
        
        (fields, expected_form)= formUtil.validate(request.POST)
        
        if len(expected_form) > 0:
            messages.error(request,expected_form)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        UserHelper.generate_and_create_user(fields)
        
        return redirect('userIndex')

class UserBaseDatatableView(BaseDatatableView):
    model = User
    columns = ['id', 'name', 'email', 'createdAt']
    max_display_length = 10
    
    def get_filter_method(self):            
        return 'icontains'
      
    def prepare_results(self, qs):
        data = []
        for item in qs:
            if not self.is_data_list:
                
                row = {'id': item.id,
                       'name': item.name, 
                       'email': item.email,
                       'company': item.company.name if item.company else '-',
                       'createdAt': item.createdAt.strftime("%d-%m-%Y %H:%M")}
                                
                data.append(row)
                
        return data