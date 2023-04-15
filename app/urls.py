from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('create/', views.create_today, name='create_today'),
    path('', views.today_index, name='today_index'),
    # path('feed/', views.today_feed, name='today_feed'),
    path('<int:today_pk>/', views.today_detail, name='today_detail'),
    path('<int:today_pk>/update/', views.update_today, name='update_today'),
    path('<int:today_pk>/delete/', views.delete_today, name='delete_today'),

    path('<int:today_pk>/todo_list/create/',views.create_todo, name='create_todo'),
    path('<int:today_pk>/replies/create/', views.create_reply, name='create_reply'),
    path('<int:today_pk>/replies/<int:reply_pk>/delete/', views.delete_reply, name='delete_reply'),
    
    
    path('<int:today_pk>/like_today/', views.like_today, name='like_today'),
    path('<int:today_pk>/sad_today/', views.sad_today, name='sad_today'),
    path('<int:today_pk>/best_today/', views.best_today, name='best_today'),
    path('<int:today_pk>/complete/', views.complete, name='complete'),
]