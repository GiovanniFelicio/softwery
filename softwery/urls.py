from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user import urls as user_urls
from home import urls as home_urls
from authentication import urls as authentication_urls

urlpatterns = [
    path('', include(home_urls)),
    path('admin/', admin.site.urls),
    path('user/', include(user_urls)),
    path('auth/', include(authentication_urls))
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
