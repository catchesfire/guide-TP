from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=5)
    confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=5)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']