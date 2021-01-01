from django.urls import path, include
from .views import listJson
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('', index, name='companyIndex'),
    # path('list/', login_required(UserBaseDatatableView.as_view()), name='companyList'),
    path('json/', listJson, name='companyListJson'),
]
