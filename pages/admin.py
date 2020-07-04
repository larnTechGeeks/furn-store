from django.contrib import admin
from .models import Furniture

class FurnitureAdmin(admin.ModelAdmin):
    list_display = ("furniture_name", "furniture_type","seller", "phone_number", "condition")
    
admin.site.register(Furniture, FurnitureAdmin)