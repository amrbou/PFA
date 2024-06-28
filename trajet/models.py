from django.db import models

from django.db import models
from client.models import Client

class Trajet(models.Model):
    pointDepart = models.CharField(max_length=100)
    pointArrivee = models.CharField(max_length=100)
    date = models.DateField()
    heure = models.TimeField()
    nbPersonnes = models.IntegerField(default=0)  
    IDClientConducteur = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='trajets_conducteur')
    passagers = models.ManyToManyField(Client, related_name='trajets_passager', blank=True)  

    def ajouter(self):
        pass
    
    def modifier(self):
        pass
    
    def supprimer(self):
        pass
    
    def __str__(self):
        return f'Trajet de {self.pointDepart} à {self.pointArrivee} le {self.date}'