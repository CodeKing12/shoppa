from django import forms
from django.utils import timezone

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control border-0 mb-3', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control border-0', 'placeholder': 'Password'}))