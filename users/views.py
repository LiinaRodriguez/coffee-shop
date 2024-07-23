from django.http import request
from django.contrib.auth.views import LoginView
from .utils import create_guest_user
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy

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

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")