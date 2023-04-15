from django.db import models
from django.contrib.auth.models import AbstractUser

from app.models import Today,Todo


class User(AbstractUser):
    like_today = models.ManyToManyField(Today, related_name='like_users')  # 테이블 추가
    sad_today = models.ManyToManyField(Today, related_name='sad_users') 
    best_today = models.ManyToManyField(Today, related_name='best_users')
    complete_today = models.ManyToManyField(Today, related_name='com_users')

    friends = models.ManyToManyField('self', symmetrical=True, related_name='friends')
    

