from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.http import HttpResponseBadRequest
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm

User = get_user_model()


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('app:today_index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()    
            login(request, user)  
            return redirect('app:today_index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def signin(request):
    if request.user.is_authenticated:
        return redirect('app:today_index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()  
            login(request, user)   
            
           
            return redirect(request.GET.get('next') or 'app:today_index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {
        'form': form,
    })


def signout(request):
    logout(request)
    return redirect('app:today_index')


@require_safe
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    friend_list = request.user.friends.filter(pk=profile_user.pk).exists()


    return render(request, 'accounts/profile.html', {
        'profile_user': profile_user,
        'friend_list': friend_list,
    })


@login_required
@require_POST
def friend(request, username):
    you = get_object_or_404(User, username=username)
    me = request.user
    if me == you:
        return HttpResponseBadRequest('error')
    
    if me.friends.filter(pk=you.pk).exists():
        me.friends.remove(you)
    else:
        me.friends.add(you)
   
    return redirect('accounts:profile', you.username)