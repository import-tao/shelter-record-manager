from django.shortcuts import render
from .models import AnimalInstance
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

# Create your views here.

def homepage(request):
    return render(request, 'catalog/homepage.html')

class AnimalDetailView(DetailView):
    model = AnimalInstance
    #template_name = "TEMPLATE_NAME"