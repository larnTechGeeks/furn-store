from django.urls import path
from .views import index, contact, about, funitures_list

urlpatterns = [
    path('', index, name="furn-home"),
    path('about/',about, name='about'),
    path('contact/', contact, name='contact'),
    path('funitures/', funitures_list, name="furnitures" )
]