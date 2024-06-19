from django.urls import path
from trajet import views

urlpatterns = [
    path('publier/', views.publier_trajet, name='publier_trajet'),
    path('recherche/', views.recherche, name='recherche'),
    path('reserver/<int:trajet_id>/', views.reserver, name='reserver'),
]
