from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Signup(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter username',
        'class': 'w-full py-2 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter email',
        'class': 'w-full py-2 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
        'class': 'w-full py-2 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password again',
        'class': 'w-full py-2 px-6 rounded-xl'
    }))