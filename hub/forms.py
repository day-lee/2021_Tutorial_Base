from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm
from .models import Curriculum
from django.contrib.auth.forms import (
                        UserCreationForm,
                        UserChangeForm,
                        PasswordChangeForm)



class GoalForm(forms.ModelForm):

    class Meta:
        model       = Profile
        fields      = ( 'goal',)


class EditProfileForm(UserChangeForm):
    email           = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name      = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name       = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username        = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model       = User
        fields      = ('username', 'password', 'first_name', 'last_name', 'email', )


class PasswordEditForm(PasswordChangeForm):
    old_password    = forms.CharField(max_length=100,
                                      widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1   = forms.CharField(max_length=100,
                                      widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2   = forms.CharField(max_length=100,
                                      widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model       = User
        fields      = ('old_password', 'new_password1', 'new_password2', )