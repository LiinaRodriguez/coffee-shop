from django.shortcuts import redirect, render
from guest_user.decorators import allow_guest_user

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

@allow_guest_user
def welcome(request):
    if request.user.is_authenticated:
        return render(request, 'core/welcome_page.html')
    else:
        return redirect('/')