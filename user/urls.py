from django.urls import path, include
from .views import UserBaseDatatableView,index,update,delete,UserCreateView,find
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name='indexUser'),
    path('list/', login_required(UserBaseDatatableView.as_view()), name='userList'),
    path('create/', login_required(UserCreateView.as_view()), name="userCreate"),
    path('find/', find, name="userFind"),
    path('update/<id>', update, name="updateUser"),
    path('delete/<id>', delete, name="deleteUser"),
]
