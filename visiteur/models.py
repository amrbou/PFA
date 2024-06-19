from django.db import models

from django.db import models

class Visiteur(models.Model):
    idVisiteur = models.CharField(max_length=100, primary_key=True)
    nomAleatoire = models.CharField(max_length=100)

    def rechercherTrajetSansDetails(self):
        pass
    
    def inscription(self):
        pass
    def __str__(self):
        return self.nomAleatoire
