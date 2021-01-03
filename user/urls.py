from django.urls import path, include
from .views import UserBaseDatatableView,UserCreateView,find,UserIndexView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(UserIndexView.as_view()), name='userIndex'),
    path('list/', login_required(UserBaseDatatableView.as_view()), name='userList'),
    path('create/', login_required(UserCreateView.as_view()), name="userCreate"),
    path('find/', find, name="userFind")
]
