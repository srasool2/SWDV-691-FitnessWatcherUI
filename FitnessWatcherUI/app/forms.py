from app.models import Profile
from django.contrib.auth.models import User
from django import forms
from string import Template
from django.utils.safestring import mark_safe
from django.conf import settings

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['weight', 'height', 'fat_percentage', 'age', 'target']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))
    class Meta:
        model=User
        help_texts = {
            'username': None,
        }
        labels={'username':'Username'}
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
