from django import forms

from .models import Register
class MyForm(forms.Form):
   password = forms.CharField(widget=forms.PasswordInput)
   Meta=Register