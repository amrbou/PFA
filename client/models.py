from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256,default='default_password')
    historiqueTrajets = models.TextField(blank=True,null=True)
    commentaires = models.TextField(blank=True, null=True)
    estConducteur = models.BooleanField(default=False)
    permis_conduire = models.FileField(upload_to='permis_conduire/', null=True, blank=True)

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
