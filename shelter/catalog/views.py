from django.shortcuts import render, render_to_response, reverse
from django.http import HttpResponseRedirect
from .models import AnimalInstance, Animal
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from . import forms

# Create your views here.
'''
To do:
- Home page showing the main information
- List of animals currently available DONE
- List of animals not in available
- Page for each animal DONE
- List of animals in each cage 
- Create new animal DONE
- delete an animal DONE
- Maintain/update Animal DONE
- Maintain animal type, colour and species = Should we split the Animal model so it only contains Species as char field. Breed is char field in its own model and
 colour remains in its own model but gets linked straight into AnimalInstance model
'''
# Homepage to show a list of all available animals
def homepage(request):
    animal_instances_available= AnimalInstance.objects.filter(status__exact='a')

    context_dict = {
        "animal_instances_available": animal_instances_available,
    }
    return render(request, 'catalog/homepage.html', context= context_dict)

class AnimalDetailView(DetailView):
    model = AnimalInstance
    template_name = 'catalog/animaldetail.html'
    context_object_name = 'animal_instance'

# View to render a create form which combines fields from more than one model. If it 
# was just one model, then a simplier, CreateView would have been used instead

def AnimalCreateView(request):
    # Check to see if a POST has been submitted. Using GET to submit forms?
    # Don't do it. Use POST.
    if request.POST:
        # Load up our two forms using the prefix keyword argument.
        # prefix is needed as there is more than one model for the page
        form = forms.AnimalCreateForm(request.POST, prefix="ani")
        sub_form = forms.AnimalInstanceCreateForm(request.POST, prefix="loc")

        # Ensure both forms are valid before continuing on
        if form.is_valid() and sub_form.is_valid():
            # Prepare the animal model, but don't commit it to the database
            # just yet.
            animal = form.save(commit=False)

            # Add the location ForeignKey by saving the secondary form we
            # setup
            animal.species = sub_form.save()

            # Save the main object and continue on our merry way.
            animal.save()
            # After a post request, you redirect to another page to prevent a continous loop of posting
            return HttpResponseRedirect(reverse('home_page') )
    
    # This will capture get request
    else:
        # set the forms to show
        form = forms.AnimalCreateForm(prefix="sch")
        sub_form = forms.AnimalInstanceCreateForm(prefix="loc") 
        # return the forms in the render to the animalcreate.html file
        # Within the template all we need to do then is {{ type form.as_p }} & {{}} sub_form.as_p }}
        return render(request, 'catalog/animalcreate.html', context={
            'form': form,
            'sub_form': sub_form,
            })

# View for updating the Animal Model
class AnimalTypeUpdateView(UpdateView):
    model = Animal
    fields = '__all__'

# View for updating the AnimalInstance Model
class AnimalInstanceUpdateView(UpdateView):
    model = AnimalInstance
    fields = '__all__'
    template_name = 'catalog/animal_instance_update.html'

class AnimalInstanceDeleteView(DeleteView):
    model = AnimalInstance
    context_object_name = 'animal_instance'
    # When deleted, it will go back to the page you specify in success_url
    success_url = reverse_lazy('home_page')
    template_name = 'catalog/animal_instance_delete.html'
