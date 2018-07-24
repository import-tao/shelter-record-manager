from django.shortcuts import render, render_to_response, reverse
from django.http import HttpResponseRedirect
from .models import AnimalInstance, Animal, Building
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Count
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
    count_available = animal_instances_available.count()
    animal_instances_reserved = AnimalInstance.objects.filter(status__exact='r')
    count_reserved = animal_instances_reserved.count()
    animal_instances_adopted = AnimalInstance.objects.filter(status__exact='d')
    count_adopted = animal_instances_adopted.count()
    context_dict = {
        'animal_instances_available': animal_instances_available,
        'count_available':count_available,
        'animal_instances_reserved':animal_instances_reserved,
        'count_reserved':count_reserved,
        'count_adopted':count_adopted,
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

class CageUpdateView(UpdateView):
    model = Building
    fields = '__all__'
    template_name = 'catalog/cage_update.html'

class AnimalInstanceDeleteView(DeleteView):
    model = AnimalInstance
    context_object_name = 'animal_instance'
    # When deleted, it will go back to the page you specify in success_url
    success_url = reverse_lazy('home_page')
    template_name = 'catalog/animal_instance_delete.html'

class CageDeleteView(DeleteView):
    model = Building
    context_object_name = 'cage'
    # When deleted, it will go back to the page you specify in success_url
    success_url = reverse_lazy('home_page')
    template_name = 'catalog/cage_delete.html'

def CageCreateView(request):
    form = forms.BuildingCreateForm()
    if request.method == 'POST':
        form = forms.BuildingCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home_page') )
        else:
            error_message = 'This room and cage already exist'
            form = forms.BuildingCreateForm()
            return render(request, 'catalog/cage_create.html', context= {'form':form, 'error':error_message})

    else:
        form = forms.BuildingCreateForm()
        return render(request, 'catalog/cage_create.html', context={
            'form': form,
            })

def cagedetailview(request):
    occupied_cages = AnimalInstance.objects.all().filter(status__exact='a').filter(cage__isnull=False)
    # Check if the cage stated is already occupied.
    # get the cage from the form and then see if it exists in the below queryset -
    # https://stackoverflow.com/questions/6554481/how-to-see-if-a-value-or-object-is-in-a-queryset-field
    #Building.objects.filter(animalanstance__status='a')
    unallocated_animals = AnimalInstance.objects.filter(status__exact='a').filter(cage__cage__isnull=True)
    vacant_cages = Building.objects.all().exclude(animalinstance__status='a')
    context = {
        'occupied_cages':occupied_cages,
        'unallocated_animals': unallocated_animals,
        'vacant_cages': vacant_cages,
    }
    return render(request, 'catalog/cage_detail.html',context)
