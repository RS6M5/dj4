from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import re


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']
        # Проверка допустимых символов
        if not re.match(r'^[\w.@+-]+$', username):
            raise ValidationError(
                "Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.")
        return username