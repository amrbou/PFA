from django.db import models

class Administrateur(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    nomAdmin = models.CharField(max_length=100)
    emailAdmin = models.EmailField(unique=True)
    password = models.CharField(default='defaultAdminPass',max_length=128)

    def authentifier(self):
        pass
    
    def gererClient(self):
        pass
    
    def gererTrajet(self):
        pass
    
    def gererProfilClient(self):
        pass
    
    def gererCommentaire(self):
        pass
    
    def bannirCompte(self):
        pass
    
    def suspendreCompte(self):
        pass
    
    def verifierIdentite(self):
        pass

    def __str__(self):
        return self.nomAdmin