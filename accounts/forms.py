from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from .models import *

class UserSignupForm (UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

class AccountEditForm (ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        exclude = ['user', 'date_created']