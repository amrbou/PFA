# forms.py
from django import forms
from administrateur.models import Administrateur

class AdminConnexionForm(forms.Form):
    emailAdmin = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')
