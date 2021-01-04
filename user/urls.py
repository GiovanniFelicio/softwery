from django.urls import path, include
from .views import UserBaseDatatableView,find
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('list/', login_required(UserBaseDatatableView.as_view()), name='userList'),
    path('find/', find, name="userFind")
]
