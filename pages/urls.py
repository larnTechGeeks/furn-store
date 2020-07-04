from django.urls import path
from .views import (
    index, 
    contact, 
    about, 
    funitures_list,
    HomeListView,
    FurnitureListView,
)

urlpatterns = [
    path('', HomeListView.as_view(), name="furn-home"),
    path('about/',about, name='about'),
    path('contact/', contact, name='contact'),
    path('funitures/', FurnitureListView.as_view(), name="furnitures" )
]