from django.http import HttpResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from django_datatables_view.base_datatable_view import BaseDatatableView
from .helper import UserHelper
from softwery.utils import formUtil
from django.contrib import messages

from user.models import User
from rest_framework import viewsets, views
from rest_framework import permissions, authentication
from user.serializer import UserSerializer
from rest_framework.response import Response

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication]

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(instance=users, many=True)
        return Response(serializer.data)

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
