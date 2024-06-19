from django.db import models


class Client(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    historiqueTrajets = models.TextField()
    estConducteur = models.BooleanField(default=False)

    def modifierInformationsCompte(self):
        pass
    
    def supprimerTrajet(self):
        pass
    
    def reserverTrajet(self):
        pass
    
    def rechercherTrajet(self):
        pass
    
    def laisseCommentaire(self):
        pass
    
    def payerTrajet(self):
        pass
    
    def gererTrajet(self):
        pass
    
    def seDeconnecter(self):
        pass
    
    def __str__(self):
        return self.nom
