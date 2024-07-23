from django.urls import path
from .views import HomeView, Welcome
from django.contrib.auth.views import LoginView

urlpatterns = [
   path('', HomeView),
   path('Home/', Welcome),
   path(
      'login/', 
      LoginView.as_view(template_name='users/login.html'), 
      name="login"
      )
]
