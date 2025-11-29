from django.contrib import admin
from .models import Leader   # import both models

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'party', 'website')
    search_fields = ('name', 'party', 'website')
