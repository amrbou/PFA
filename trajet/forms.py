from django import forms
from .models import Trajet
from django.core.exceptions import ValidationError
from datetime import date

class RechercheForm(forms.Form):
    pointDepart = forms.CharField(max_length=100, label='Départ')
    pointArrivee = forms.CharField(max_length=100, label='Destination')
    date = forms.DateField(widget=forms.SelectDateWidget, label='Date')
    nbPersonnes = forms.IntegerField(min_value=1, label='Nombre total de personnes')

class TrajetForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  
    heure = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Trajet
        fields = ['pointDepart', 'pointArrivee', 'date', 'heure', 'nbPersonnes']

    def clean_date(self):
        selected_date = self.cleaned_data['date']
        if selected_date < date.today():
            raise ValidationError("La date ne peut pas être dans le passé.")
        return selected_date