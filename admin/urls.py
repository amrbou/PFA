from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.admin_inscription, name='admin_inscription'),
    path('connexion/', views.admin_connexion, name='admin_connexion'),
    path('verification_permis/', views.verification_permis, name='verification_permis'),
    path('verifier_permis/<int:permis_id>/', views.verifier_permis, name='verifier_permis'),
]
