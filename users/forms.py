from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
            super(UserCreateForm, self).__init__(*args, **kwargs)
            self.fields['username'].help_text = 'Massimo 150 caratteri. Non può contenere caratteri speciali.'
            self.fields['email'].help_text = "Inserire un'email valida."
            self.fields['password1'].help_text = 'La password deve contenere almeno 8 caratteri.'
            self.fields['password2'].help_text = 'Inserire la stessa password'
        
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
