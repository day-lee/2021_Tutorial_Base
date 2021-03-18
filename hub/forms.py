from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Curriculum
from django.contrib.auth.forms import UserCreationForm, UserChangeForm




class GoalForm(forms.ModelForm):

    class Meta:
        model = Curriculum
        fields = '__all__' #('goal',)


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email',  )