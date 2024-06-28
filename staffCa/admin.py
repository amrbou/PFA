from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_admin')
    search_fields = ('email',)
    list_filter = ('is_active', 'is_admin')
