from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user import urls as user_urls
from home import urls as home_urls

urlpatterns = [
    path('', include(home_urls)),
    path('admin/', admin.site.urls),
    path('user/', include(user_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
