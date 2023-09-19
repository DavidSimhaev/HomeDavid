from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

from django.contrib.auth import authenticate, login, logout



def register(request):
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'users/register.html', context)
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        __user = form.cleaned_data.get('username')
        __password = form.cleaned_data.get('password2')
        user = authenticate(request, username=__user, password=__password)
        login(request, user)
        messages.success(request, 'Account was created for ' + __user)
        return redirect('Main:Main')
    else:
        print('Form is not valid')
        messages.error(request, 'Error Processing Your Request')
        context = {'form': form}
        return render(request, 'users/register.html', context)
