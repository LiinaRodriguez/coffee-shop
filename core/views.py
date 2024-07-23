from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
def welcome(request):
    if request.user.is_authenticated:
        return render(request, 'core/welcome_page.html')
    else:
        return redirect('/')