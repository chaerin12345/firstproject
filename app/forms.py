from django import forms
from .models import Today, Reply,Todo

class TodayForm(forms.ModelForm):

    class Meta:
        model = Today
        # user 빼고 모든 필드 다
        exclude = ('user', )


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ('content', )


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('todo_content','todo_complete', )