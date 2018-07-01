from django.shortcuts import render
from .models import AnimalInstance
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

# Create your views here.
'''
To do:
- Home page showing the main information
- List of animals currently available
- List of animals not in available
- Page for each animal
- List of animals in each cage
- Create new animal
- delete an animal
- Maintain/update Animal
'''

def homepage(request):
    return render(request, 'catalog/homepage.html')

class AnimalDetailView(DetailView):
    model = AnimalInstance
    #template_name = "TEMPLATE_NAME"