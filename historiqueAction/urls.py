from django.urls import path
from . import views

urlpatterns = [
    path('', views.historique_action, name='historique_action'),
]
