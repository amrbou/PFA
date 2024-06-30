from django.urls import path
from trajet import views

urlpatterns = [
    path('recherche/', views.recherche, name='recherche'),
    path('reserver/<int:trajet_id>/', views.reserver, name='reserver'),
    path('publier/', views.publier_trajet, name='publier_trajet'),
    path('error_not_conductor/', views.error_not_conductor, name='error_not_conductor'),
    path('changer_destination/<int:trajet_id>/', views.changer_destination, name='changer_destination'),
    path('annuler_trajet/<int:trajet_id>/', views.annuler_trajet, name='annuler_trajet'),
    path('mes_trajets/', views.mes_trajets, name='mes_trajets'),
    path('modifier_trajet/<int:trajet_id>/', views.modifier_trajet, name='modifier_trajet'),
    path('annuler_reservation/<int:trajet_id>/', views.annuler_reservation, name='annuler_reservation'),
]
