from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count

from .models import Today, Reply, Todo
from .forms import TodayForm, ReplyForm, TodoForm


@login_required
@require_http_methods(['GET', 'POST'])
def create_today(request):
    if request.method == 'POST':
        form = TodayForm(request.POST)
        todo_form = TodoForm(request.POST)
    
        if form.is_valid():
            today = form.save(commit=False)
            today.user = request.user
            today.save()
            return redirect('app:today_detail', today.pk)
    else:
        form = TodayForm()
        todo_form = TodoForm()
    return render(request, 'app/form.html', {
        'form': form,
        'todo_form':todo_form,
    })


@require_safe
def today_index(request):
    todays = Today.objects.all()
    paginator = Paginator(todays, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app/index.html', {
        'page_obj': page_obj,
    })


# @login_required
# @require_safe
# def today_feed(request):
#     user = request.user
#     todays = Today.objects.filter(user__in=user.stars.all())
    

#     return render(request, 'app/index.html', {
#         'todays': todays,
#     })



@require_http_methods(['GET', 'HEAD'])
def today_detail(request, today_pk):
    today = get_object_or_404(Today, pk=today_pk)
    todo_list = today.todo_set.all()
    replies = today.reply_set.all()
    form = ReplyForm()
    form2 = TodoForm()
    is_like = today.like_users.filter(pk=request.user.pk).exists()
    is_sad = today.sad_users.filter(pk=request.user.pk).exists()
    is_best = today.best_users.filter(pk=request.user.pk).exists()
    # is_complete = today.com_users.filter(pk=request.user.pk).exists()
    
    return render(request, 'app/detail.html', {
        'today': today,
        'replies': replies,
        'form': form,
        'form2':form2,
        'is_like': is_like,
        'is_sad':is_sad,
        'is_best':is_best,
        # 'todo':todo,
        'todo_list':todo_list,
        # 'is_complete':is_complete,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def update_today(request, today_pk):
    today = get_object_or_404(Today, pk=today_pk)

    if request.user != today.user:
        return redirect('app:today_index')

    if request.method == 'POST':
        form = TodayForm(request.POST, instance=today)
        if form.is_valid():
            today = form.save()
            return redirect('app:today_detail', today.pk)
    else:
        form = TodayForm(instance=today)
    return render(request, 'app/form.html', {
        'form': form,
    })


@login_required
@require_POST
def delete_today(request, today_pk):
    today = get_object_or_404(Today, pk=today_pk)
    
    if request.user != today.user:
        return redirect('app:today_index')
        
    today.delete()
    return redirect('app:today_index')


@login_required
@require_POST
def create_reply(request, today_pk):
    today = get_object_or_404(Today, pk=today_pk)
    form = ReplyForm(request.POST)

    if form.is_valid():
        reply = form.save(commit=False)  
        reply.today = today  
        reply.user = request.user
        reply.save()
    return redirect('app:today_detail', today.pk)
    
@login_required
@require_POST
def delete_reply(request, today_pk, reply_pk):
    today = get_object_or_404(Today, pk=today_pk)
    reply = get_object_or_404(Reply, pk=reply_pk)

    if request.user == reply.user:
        reply.delete()
        
    return redirect('app:today_detail', today.pk)

def create_todo(request, today_pk):
    today = get_object_or_404(Today, pk=today_pk)
    form = TodoForm(request.POST)

    if form.is_valid():
        todo = form.save(commit=False) 
        todo.today = today  
        todo.user = request.user
        todo.save()
        return redirect('app:today_detail', today.pk)
    else:
        form = TodoForm()
        
    return render(request,'app/form.html',{
        'form':form,
        
    })

@login_required
@require_POST
def like_today(request, today_pk):
    today = get_object_or_404(Today, pk=today_pk)
    user = request.user

    if today.like_users.filter(pk=user.pk).exists():  
        today.like_users.remove(user)
    else:
        today.like_users.add(user)
    return redirect('app:today_detail', today.pk)

@login_required
@require_POST
def sad_today(request, today_pk):
    today = get_object_or_404(Today, pk=today_pk)
    user = request.user

    if today.sad_users.filter(pk=user.pk).exists():  
        today.sad_users.remove(user)
    else:
        today.sad_users.add(user)
    return redirect('app:today_detail', today.pk)

@login_required
@require_POST
def best_today(request, today_pk):
    today = get_object_or_404(Today, pk=today_pk)
    user = request.user

    if today.best_users.filter(pk=user.pk).exists():  
        today.best_users.remove(user)
    else:
        today.best_users.add(user)
    return redirect('app:today_detail', today.pk)

@login_required
@require_POST
def complete(request, today_pk):
    today = get_object_or_404(Today, pk=today_pk)
    is_complete = today.com_users.filter(pk=request.user.pk).exists()
    # is_complete = Todo.todo_complete(value=True)
    return redirect('app:today_detail', today.pk ,{
        'is_complete':is_complete,
    })