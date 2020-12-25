from django.urls import path
from .views import index,create,update,delete

urlpatterns = [
    path('', index, name='indexUser'),
    path('create/', create, name="createUser"),
    path('update/<id>', update, name="updateUser"),
    path('delete/<id>', delete, name="deleteUser"),
]
