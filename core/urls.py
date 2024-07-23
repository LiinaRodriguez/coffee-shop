from .views import home, welcome
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', home, name='home'),
   path('welcome/', welcome, name='welcome'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
