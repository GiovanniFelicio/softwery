from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user import urls as user_urls
from home import urls as home_urls
from company import urls as company_urls
from authentication import urls as authentication_urls

from django.conf import settings
from rest_framework import routers
from softwery import views
from company.views import CompanyViewSet, CompanyApiView
from user.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'company', CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('teste2/', CompanyApiView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('teste/', include(home_urls)),
    path('admin/', admin.site.urls),
    path('user/', include(user_urls)),
    path('companies/', include(company_urls)),
    path('auth/', include(authentication_urls))
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns