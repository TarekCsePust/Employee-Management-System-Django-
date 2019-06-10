from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model,authenticate,login
User = get_user_model()

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First name',required=True)
    last_name = forms.CharField(label='Last name',required=True)
    email = forms.EmailField(label='Email address',required=True)
    class Meta:
        model = User
        fields=[
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]


class LoginForm(forms.Form):
    username = forms.CharField(label='username',required=True)
    password =forms.CharField(widget=forms.PasswordInput,required=True,label='password')

class ProfileUpadteForm(forms.Form):
    first_name = forms.CharField(label='First name',required=True)
    last_name =forms.CharField(label="Last name",required=True)
    email = forms.EmailField(label='Email address',required=True)

    class Meta:
        model = User
        fields=[
            'first_name',
            'last_name',
            'email'
        ]

    

   

