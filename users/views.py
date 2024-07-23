from django.http import request
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .utils import create_guest_user
from django.shortcuts import redirect
from django.contrib.auth import login

# Create your views here.
class CustomLoginView(LoginView):
    template_name='users/login.html'
    def post(self, request, *args, **kwargs):
        if 'guest_login' in request.POST:

            guest_user = create_guest_user()
            login(request, guest_user)
            return redirect('/')
        else:
            return super().post(request, *args, **kwargs)

def HomeView(request):
    return render(request, 'home.html')

def Welcome(request):
    return render(request, 'home.html')