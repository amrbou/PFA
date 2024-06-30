from django.db import models
from datetime import timedelta, datetime
from django.utils import timezone
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


    def peut_etre_annule(self):
        trajet_datetime = datetime.combine(self.date, self.heure)
        if timezone.now() < trajet_datetime - timedelta(hours=24):
            return True
        return False
 
    def est_complet(self):
        return self.nbPersonnes <= 0
    
    def ajouter(self):
        pass
    
    def modifier(self):
        pass
    
    def supprimer(self):
        pass
    
    def __str__(self):
        return f'Trajet de {self.pointDepart} à {self.pointArrivee} le {self.date}'
    
