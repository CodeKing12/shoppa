from django import forms
from django.utils import timezone
from .models import CustomAccount

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control border-0 mb-3', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control border-0', 'placeholder': 'Password'}))

class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = CustomAccount
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(CreateAccountForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'id':'register_email', 'placeholder':'Email'})
        self.fields['password'].widget = forms.TextInput(attrs={'id':'register_pass', 'placeholder':'Password'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder':'First Name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder':'Last Name'})
        self.fields['phone_number'].widget = forms.TextInput(attrs={'placeholder':'Phone Number'})
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control border-0 mb-3'