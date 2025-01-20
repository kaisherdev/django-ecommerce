from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.

def register(request):
    form = RegistrationForm()
    contex = {
        'form':form,
    }
    return render(request,'accounts/register.html',contex)

def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    pass
    # return render(request,'accounts/logout.html')s