from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nome = forms.CharField(max_length=30, required=False)
    cognome = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ("username","nome", "cognome", "email", "password1", "password2")
