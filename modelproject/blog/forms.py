from dataclasses import fields
from django import forms
from .models import Blog,Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'writer', 'body', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_body']