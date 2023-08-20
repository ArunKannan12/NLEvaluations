from django import forms
from django.forms import ModelForm
from .models import *
from django.utils.translation import gettext,gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class': 'form-control form-control-lg'}))
    password = forms.CharField(label=_("password"),strip=False,widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg','autocomplete':'current-password'}))

class RegistrationForm(UserCreationForm):
    username=forms.CharField(label='username',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter user name'}))
    email=forms.EmailField(label='Enter email',required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter E-mail'}))
    password1=forms.CharField(label='Enter password',required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))
    password2=forms.CharField(label='Re-enter password',required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("An user with this email already exists!")
        return email


class admin_task_form(forms.ModelForm):
    app_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'App name','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    points=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'points','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    class Meta:
        model = admin_task
        fields =['app_name','image','app_category','sub_category','points']
