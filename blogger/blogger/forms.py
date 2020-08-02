from django import forms
from django.contrib.auth.models import User


class SignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


    def clean_email(self):
        current_email = self.cleaned_data.get('email')
        user = User.objects.filter(email=current_email)

        if user.exists():
            raise forms.ValidationError("User with email already exists")
        else:
            return current_email