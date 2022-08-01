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
        # del self.fields['password1']
        # del self.fields['password2']

    # def save(self, *args, **kwargs):
    #     if self.fields['mobile_number']:
    #         self.fields['otp'] = str(random.randint(1000, 9999))
    #     super(CustomUserCreationForm, self).save(*args, **kwargs)
        
    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = super(UserCreationForm, self).clean_password2()
    #     if bool(password1) ^ bool(password2):
    #         raise forms.ValidationError("Fill out both fields")
    #     return password2
class LoginFormView(forms.Form):
    # class Meta:
    #     model = CustomUser
    #     fields = ['email', 'mobile_number']
        
    # email = forms.CharField(label='Email')
    mobile_number = forms.CharField(label='Registered Mobile Number')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'mobile_number']

class OTPForm(forms.Form):
    otp = forms.CharField(label='OTP')