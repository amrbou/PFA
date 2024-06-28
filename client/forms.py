from django import forms
from client.models import Client

class InscriptionForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ['nom', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Client.objects.filter(email=email).exists():
            raise forms.ValidationError("Un compte avec cette adresse e-mail existe déjà.")
        return email

class ConnexionForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ['email', 'password']

class CompteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    current_password = forms.CharField(widget=forms.PasswordInput, required=True, label='Mot de passe actuel')
    permis_conduire = forms.FileField(required=False)

    class Meta:
        model = Client
        fields = ['nom', 'email', 'password', 'permis_conduire', 'phone', 'profile_picture']

class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom','email','permis_conduire', 'estConducteur']