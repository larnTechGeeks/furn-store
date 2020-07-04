from django.urls import path
from .views import (
    index, 
    contact, 
    about, 
    funitures_list,
    HomeListView,
    FurnitureListView,
    FurnitureDetailView,
)

urlpatterns = [
    path('', HomeListView.as_view(), name="furn-home"),
    path('about/',about, name='about'),
    path('contact/', contact, name='contact'),
    path('funitures/', FurnitureListView.as_view(), name="furnitures" ),
    path('furniture/<int:pk>/',FurnitureDetailView.as_view(), name='furniture_detail')
]