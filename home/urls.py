from django.urls import path, include
from .views import index
from .views import doLogout
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', index, name='indexHome'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', doLogout, name='logout')
]
