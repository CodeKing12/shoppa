from django import forms
from django.utils import timezone
from accounts.models import Login

class LoginForm(forms.ModelForm):
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Login
        fields = ["email", "password"]