from django import forms
from django.utils import timezone
from .models import CustomAccount

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class CreateAccountForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"id": "second-password", "placeholder": "Confirm Password"}))

    class Meta:
        model = CustomAccount
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']

    def __init__(self, *args, **kwargs):
        super(CreateAccountForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'id':'register_email', 'placeholder':'Email', 'type': 'email'})
        self.fields['password'].widget = forms.TextInput(attrs={'id':'register_pass', 'placeholder':'Password', 'type': 'password'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder':'First Name', 'type': 'text'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder':'Last Name', 'type': 'text'})
        self.fields['phone_number'].widget = forms.TextInput(attrs={'placeholder':'Phone Number', 'type': 'tel'})
        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'form-control border-0 mb-3'

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    state = forms.ChoiceField()
    street_address = forms.CharField(max_length=300)
    city = forms.CharField(max_length=200)
    postcode = forms.IntegerField()
    email = forms.EmailField()
    phone = forms.IntegerField()