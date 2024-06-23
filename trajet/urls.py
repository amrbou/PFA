from django.urls import path
from trajet import views

urlpatterns = [
    path('recherche/', views.recherche, name='recherche'),
    path('reserver/<int:trajet_id>/', views.reserver, name='reserver'),
    path('publier/', views.publier_trajet, name='publier_trajet'),
    path('error_not_conductor/', views.error_not_conductor, name='error_not_conductor'),
]
