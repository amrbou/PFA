from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('index/', views.index, name='index'),
    path('home/<int:client_id>/', views.home, name='home_with_id'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('compte/', views.compte, name='compte'),
    path('mes_trajets/', views.mes_trajets, name='mes_trajets'),
]
