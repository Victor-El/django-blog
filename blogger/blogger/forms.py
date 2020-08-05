from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class SignInForm(forms.Form):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={
        "placeholder": "email"
    }))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        "placeholder": "password"
    }))

    def clean(self):
        data = self.cleaned_data
        user = authenticate(username=data['email'], password=data['password'])
        if user == None:
            raise forms.ValidationError('Incorrect email or password')
        return data


class SignUpForm(forms.Form):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={
        "placeholder": "email"
    }))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        "placeholder": "password"
    }))


    def clean_email(self):
        current_email = self.cleaned_data.get('email')
        user = User.objects.filter(email=current_email)

        if user.exists():
            raise forms.ValidationError("User with email already exists")
        else:
            return current_email