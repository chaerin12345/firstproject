from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

WEATHER_CHOICES = [
    ('맑음','맑음'),
    ('흐림','흐림'),
    ('비', '비'),
    ('눈','눈'),

]

# 오늘의 일기 및 투두리스트 
class Today(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # todo_list_content = models.CharField(max_length=200)
    # todo_list_complete = models.BooleanField(default=False)
    date = models.DateField()
    weather = models.CharField(max_length=200, choices= WEATHER_CHOICES)

# 댓글 달기 
class Reply(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    today = models.ForeignKey(Today, on_delete = models.CASCADE)


class Todo(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    todo_content = models.CharField(max_length=200)
    todo_complete = models.BooleanField(default=False)
    today = models.ForeignKey(Today, on_delete = models.CASCADE)
    
