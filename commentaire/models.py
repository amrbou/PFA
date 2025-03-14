from django.db import models
from client.models import Client

class Commentaire(models.Model):
    id = models.AutoField(primary_key=True)
    texte = models.TextField()
    notation = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='commentaire_set')

    def ajouter(self):
        pass
    
    def modifier(self):
        pass
    
    def supprimer(self):
        pass

    def __str__(self):
        return f'Commentaire de {self.clientID.nom} le {self.date}'