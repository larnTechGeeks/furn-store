from django.contrib import admin
from .models import Furniture

class FurnitureAdmin(admin.ModelAdmin):
    list_display = ("furn_name", "furn_type","seller", "phone_number", "condition")
    
admin.site.register(Furniture, FurnitureAdmin)