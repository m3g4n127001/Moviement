from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('movies:list')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POSt.get('next'))
            else:
                return redirect('movies:list')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('movies:list')
