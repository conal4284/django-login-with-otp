from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import CustomUser
from django import forms
from django.forms import TextInput
import random

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','email', 'mobile_number']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        self.fields['password1'].widget = forms.HiddenInput()
        self.fields['password2'].widget = forms.HiddenInput()

class LoginFormView(forms.Form):
    mobile_number = forms.CharField(label='Registered Mobile Number')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'mobile_number']

class OTPForm(forms.Form):
    otp = forms.CharField(label='OTP')