from django.urls import path
from .views import UserView, UserBaseDatatableView,index,create,update,delete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(UserView.as_view()), name='indexUser'),
    path('list/', login_required(UserBaseDatatableView.as_view()), name='userList'),
    path('create/', create, name="createUser"),
    path('update/<id>', update, name="updateUser"),
    path('delete/<id>', delete, name="deleteUser"),
]
