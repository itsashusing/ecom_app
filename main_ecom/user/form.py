from django import forms
from django.contrib.auth.models import User


class SignUpUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CheckOutForm(forms.Form):
    address=forms.CharField()
    phonenumber=forms.CharField()
    city=forms.CharField()
