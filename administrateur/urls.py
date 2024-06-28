from django.urls import path
from . import views

urlpatterns = [
    path('staff_login/', views.admin_connexion, name='staff_login'),
]