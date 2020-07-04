from django.shortcuts import render
from django.views.generic import ListView
from pages.models import Furniture
def index(request):
    template_name = 'pages/index.html'
    return render(request, template_name)

def funitures_list(request):
    template_name = 'pages/category.html'
    return render(request, template_name)

def about(request):
    pass

def contact(request):
    template_name = 'pages/contact.html'
    return render(request, template_name)
#Home_View
class HomeListView(ListView):
    model = Furniture
    template_name='pages/furn_home.html'
    context_object_name = 'furnitures'
#LISTVIEW
class FurnitureListView(ListView):
    template_name = 'pages/furnitures.html'
    context_object_name = 'furnitures'
