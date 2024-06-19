from django import forms
from .models import Trajet

class RechercheForm(forms.Form):
    pointDepart = forms.CharField(max_length=100, label='Départ')
    pointArrivee = forms.CharField(max_length=100, label='Destination')
    date = forms.DateField(widget=forms.SelectDateWidget, label='Date')
    nbPersonnes = forms.IntegerField(min_value=1, label='Nombre total de personnes')

class TrajetForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Utiliser le type HTML5 'date'

    class Meta:
        model = Trajet
        fields = ['pointDepart', 'pointArrivee', 'date', 'heure', 'nbPersonnes']
