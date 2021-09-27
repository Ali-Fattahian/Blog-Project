from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post',)
        labels = {
            'username':'Your Name',
            'email': 'Your Email',
            'comment_content':'Your Comment'
        }