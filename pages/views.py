from django.shortcuts import render

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
