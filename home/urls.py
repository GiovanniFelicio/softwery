from django.urls import path, include
from .views import index
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', index, name='homeIndex')
]
