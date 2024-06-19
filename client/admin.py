from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ['nom', 'email', 'password', 'estConducteur']

admin.site.register(Client)

