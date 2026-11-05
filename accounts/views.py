from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        next_url = request.POST.get('next') or request.GET.get('next')
        
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                if next_url:
                    return redirect(next_url)

                return redirect('/')
                
        # django built in forms
        form = AuthenticationForm()
        context = {'form':form, 'next': next_url}
    else:
        return redirect('/')
    return render(request, 'accounts/login.html',context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        form = UserCreationForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('/')
                    
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')