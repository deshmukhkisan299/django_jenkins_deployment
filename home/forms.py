from django.contrib.auth.models import User
from django import forms

class userform(forms.ModelForm):
    user = User
    fields = ['username', 'email', 'password']