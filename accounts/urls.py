from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/friend/', views.friend, name='friend'),
] 