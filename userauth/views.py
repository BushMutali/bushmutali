from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .forms import MyUserCreationForm

def user_login(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
            
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('study-room')
        else:
            messages.error(request, 'Email or Password does not exist')
        
    context ={'page':page}
    return render(request, 'userauth/login_register.html', context)

def user_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))

def user_register(request):
    page = 'register'
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Fill in the fields correctly')
        
    context = {'form': form, 'page': page}
    return render(request, 'userauth/login_register.html', context)

@login_required(login_url='home')
def user_update(request):
    context = {}
    return render(request, 'userauth/update.html', context)