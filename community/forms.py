from django import forms
from .models import Post, Category, Comment

from django.db.utils import OperationalError

try:

    choices = Category.objects.all().values_list('name', 'name')
    choice_list = []

    for item in choices:
        choice_list.append(item)

    class PostForm(forms.ModelForm):
        class Meta:
            model         = Post
            fields        = ('title', 'author', 'category', 'body')
            widgets       = {
                'title'   : forms.TextInput(attrs={'class': 'form-control'},),
                'author'  : forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'users_id', 'type': 'hidden'} ),
                'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
                'body'    : forms.Textarea(attrs={'class': 'form-control'}),
            }

    class EditForm(forms.ModelForm):
        class Meta:
            model         = Post
            fields        = ('title', 'body')
            widgets       = {
                'title'   : forms.TextInput(attrs={'class': 'form-control'}),
                'body'    : forms.Textarea(attrs={'class': 'form-control'}),
            }


    class CommentForm(forms.ModelForm):
        class Meta:
            model         = Comment
            fields        = ('name', 'body')
            widgets       = {
                'name'    : forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'users_id', 'type': 'hidden'}),
                'body'    : forms.Textarea(attrs={'class': 'form-control'}),
            }

except OperationalError:
    pass  # happens when db doesn't exist yet, views.py should be
          # importable without this side effect