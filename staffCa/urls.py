from django.urls import path
from . import views
from .views import staff_login, admin_dashboard, staff_logout, modifier_trajet, supprimer_trajet

urlpatterns = [
    path('staff_login/', views.staff_login, name='staff_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('staff_logout/', views.staff_logout, name='staff_logout'),
    path('modifier_trajet/<int:trajet_id>/', modifier_trajet, name='modifier_trajet'),
    path('supprimer_trajet/<int:trajet_id>/', supprimer_trajet, name='supprimer_trajet'),
    path('gerer_profil_client/<int:client_id>/', views.gerer_profil_client, name='gerer_profil_client'),
    path('suspendre_client/<int:client_id>/', views.suspendre_client, name='suspendre_client'),
    path('bannir_client/<int:client_id>/', views.bannir_client, name='bannir_client'),
]
