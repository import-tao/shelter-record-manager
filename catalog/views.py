from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, reverse, get_object_or_404
from django.urls import reverse_lazy, resolve
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from . import forms
from .resources import AnimalInstanceResource
from .models import AnimalInstance, Building, Allergies, Medication

# Login imports - login required is for function based views
# Mixin is for class based views and is passed as an argument

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

@login_required
def homepage_view(request):
    animal_instances_available= AnimalInstance.objects.filter(status__exact='a').order_by("-arrival_date")
    count_available = animal_instances_available.count()
    animal_instances_reserved = AnimalInstance.objects.filter(status__exact='r').order_by("-arrival_date")
    count_reserved = animal_instances_reserved.count()
    animal_instances_quarantine = AnimalInstance.objects.filter(status__exact='q').order_by("-arrival_date")
    count_quarantine = animal_instances_quarantine.count()
    animal_instances_adopted = AnimalInstance.objects.filter(status__exact='d').order_by("-arrival_date")
    count_adopted = animal_instances_adopted.count()
    cage_objects = Building.objects.all()
    count_occupied_cages = AnimalInstance.objects.all().exclude(status__exact='d') \
                    .values_list('cage__cage').distinct().exclude(cage__cage=None).count()
    count_available_cages = cage_objects.count() - count_occupied_cages

    context_dict = {
        'animal_instances_available': animal_instances_available,
        'count_available':count_available,
        'animal_instances_reserved':animal_instances_reserved,
        'count_reserved':count_reserved,
        'animal_instances_quarantine': animal_instances_quarantine,
        'count_quarantine': count_quarantine,
        'count_adopted':count_adopted,
        'animal_instances_adopted':animal_instances_adopted,
        'cage_objects': cage_objects,
        'count_occupied_cages': count_occupied_cages,
        'count_available_cages':count_available_cages,
    }
    return render(request, 'catalog/homepage.html', context= context_dict)


class AnimalDetailView(LoginRequiredMixin,DetailView):
    model = AnimalInstance
    template_name = 'catalog/animaldetail.html'
    context_object_name = 'animal_instance'


@login_required
def AnimalCreateView(request):
    # Check to see if a POST has been submitted. Using GET to submit forms?
    # Don't do it. Use POST.
    if request.POST:
        form = forms.AnimalInstanceCreateForm(request.POST)
        if form.is_valid():
            # Prepare the animal model, but don't commit it to the database
            # just yet.
            animal = form.save(commit=False)
            # Save the main object and continue on our merry way.
            animal.save()
            # After a post request, you redirect to another page to prevent a continous loop of posting
            return HttpResponseRedirect(reverse('home_page') )
    # This will capture get request
    else:
        # set the forms to show
        form = forms.AnimalInstanceCreateForm()
        # return the forms in the render to the animalcreate.html file
        # Within the template all we need to do then is {{ type form.as_p }} & {{}} sub_form.as_p }}
        return render(request, 'catalog/animalcreate.html', context={
            'form': form,
            })

# View for updating the Animal Model
@login_required
def animalinstanceadoptview(request, pk):
    url_name = resolve(request.path).url_name
    if request.method == 'POST':
        form = forms.AnimalInstanceAdoptForm(request.POST, prefix="ani", instance = get_object_or_404(AnimalInstance, id=pk))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home_page'))
        else:
            context = {
                'form':form,
            }
            if 'adopt_existing' in url_name:
                return render(request, 'catalog/adopted_animal_update', context)
            else:
                return render(request, 'catalog/adopt_animal.html', context)
    else:
        date = datetime.today().date()
        initial = {
            'leaving_date': date,
        }
        form = forms.AnimalInstanceAdoptForm(instance=get_object_or_404(AnimalInstance, id=pk), prefix="ani", initial=initial)
        context = {
            'form':form,
        }
        # Get the url which is being passed to the view, and then decide which template to use
        #This means we can still use the same view logic without repeating ourself
        if 'adopt_existing' in url_name:
            return render(request, 'catalog/adopted_animal_update.html', context)
        else:
            return render(request, 'catalog/adopt_animal.html', context)


class AnimalInstanceUpdateView(LoginRequiredMixin, UpdateView):
    model = AnimalInstance
    fields = [
            'name',
            'cross',
            'bio',
            'status',
            'arrival_date',
            'gender',
            'hair_type',
            'hair_length',
            'cage',
            'food_type',
            'portion_size',
            'daily_portions',
            'allergies',
            'picture',
        ]
    template_name = 'catalog/animal_instance_update.html'

class AdoptedAnimalUpdate(LoginRequiredMixin, UpdateView):
    queryset = AnimalInstance.objects.all()

    def get_context_data(self, **kwargs):
        _id = self.kwargs.get('id')
        context = super(AdoptedAnimalUpdate, self).get_context_data(**kwargs)
        context['second_model'] = SecondModel.objects.get(id=pk) #whatever you would like
        return context

class CageUpdateView(LoginRequiredMixin, UpdateView):
    model = Building
    fields = '__all__'
    template_name = 'catalog/cage_update.html'
    success_url = reverse_lazy('cage_detail')


class AnimalInstanceDeleteView(LoginRequiredMixin, DeleteView):
    model = AnimalInstance
    context_object_name = 'animal_instance'
    # When deleted, it will go back to the page you specify in success_url
    success_url = reverse_lazy('home_page')
    template_name = 'catalog/animal_instance_delete.html'


class CageDeleteView(LoginRequiredMixin, DeleteView):
    model = Building
    context_object_name = 'cage'
    # When deleted, it will go back to the page you specify in success_url
    success_url = reverse_lazy('home_page')
    template_name = 'catalog/cage_delete.html'

@login_required
def cagecreateview(request):
    if request.method == 'POST':
        form = forms.BuildingCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home_page') )
        else:
            return render(request, 'catalog/cage_create.html', context= {'form':form})

    else:
        form = forms.BuildingCreateForm()
        return render(request, 'catalog/cage_create.html', context={
            'form': form,
            })

@login_required
def cagedetailview(request):
# use Q to do a negative filter. Q and | can also be used for 'or' queries e.g. .filter(Q(status__exact='a') | Q(status__exact='d'))
    occupied_cages = AnimalInstance.objects.all().filter(~Q(status__exact='d')).filter(cage__isnull=False)
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

@login_required
def adopted_animals_view(request):
    animal_instances_adopted = AnimalInstance.objects.filter(status__exact='d').order_by("name")
    count_adopted = animal_instances_adopted.count()
    context_dict = {
        'animal_instances_adopted': animal_instances_adopted,
        'count_adopted': count_adopted,
        }
    return render(request, 'catalog/adopted_animals.html', context=context_dict)


@login_required
def available_animals_view(request):
    animal_instances_available = AnimalInstance.objects.filter(status__exact='a').order_by("name")
    count_available = animal_instances_available.count()
    context_dict = {
        'animal_instances_available': animal_instances_available,
        'count_available': count_available,
        }
    return render(request, 'catalog/available_animals.html', context=context_dict)


@login_required
def reserved_animals_view(request):
    animal_instances_reserved = AnimalInstance.objects.filter(status__exact='r').order_by("name")
    count_reserved = animal_instances_reserved.count()
    context_dict = {
        'animal_instances_reserved': animal_instances_reserved,
        'count_reserved': count_reserved,
        }
    return render(request, 'catalog/reserved_animals.html', context=context_dict)

@login_required
def quarantined_animals_view(request):
    animal_instances_quaratine = AnimalInstance.objects.filter(status__exact='q').order_by("name")
    count_quaratine = animal_instances_quaratine.count()
    context_dict = {
        'animal_instances_quaratine': animal_instances_quaratine,
        'count_quaratine': count_quaratine,
        }
    return render(request, 'catalog/quarantined_animals.html', context=context_dict)

@login_required
def allergycreateview(request):
    if request.method == 'POST':
        form = forms.AllergiesCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('allergy_list'))
        else:
            return render(request, reverse('allergy_create'), context = {'form':form})
    else:
        form = forms.AllergiesCreateForm()
        context = {
            'form':form,
        }
        return render(request, 'catalog/allergy_create.html', context)

@login_required
def allergylistview(request):
# use Q to do a negative filter. Q and | can also be used for 'or' queries e.g. .filter(Q(status__exact='a') | Q(status__exact='d'))
    allergies = Allergies.objects.all()
    # Check if the cage stated is already occupied.
    # get the cage from the form and then see if it exists in the below queryset -
    # https://stackoverflow.com/questions/6554481/how-to-see-if-a-value-or-object-is-in-a-queryset-field
    #Building.objects.filter(animalanstance__status='a')
    context = {
        'allergies': allergies,
    }
    return render(request, 'catalog/allergies_list.html', context)

class AllergyDeleteView(LoginRequiredMixin, DeleteView):
    model = Allergies
    context_object_name = 'allergy'
    # When deleted, it will go back to the page you specify in success_url
    success_url = reverse_lazy('allergy_list')
    template_name = 'catalog/allergy_delete.html'



@login_required
def medicationcreateview(request):
    if request.method == 'POST':
        form = forms.MedicationCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('medication_list'))
        else:
            return render(request, reverse('medication_create'), context = {'form':form})
    else:
        form = forms.MedicationCreateForm()
        context = {
            'form':form,
        }
        return render(request, 'catalog/medication_create.html', context)

@login_required
def medicationlistview(request):
# use Q to do a negative filter. Q and | can also be used for 'or' queries e.g. .filter(Q(status__exact='a') | Q(status__exact='d'))
    medication = Medication.objects.all()
    # Check if the cage stated is already occupied.
    # get the cage from the form and then see if it exists in the below queryset -
    # https://stackoverflow.com/questions/6554481/how-to-see-if-a-value-or-object-is-in-a-queryset-field
    #Building.objects.filter(animalanstance__status='a')
    context = {
        'medication': medication,
    }
    return render(request, 'catalog/medication_list.html', context)

class MedicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Medication
    context_object_name = 'medication'
    # When deleted, it will go back to the page you specify in success_url
    success_url = reverse_lazy('medication_list')
    template_name = 'catalog/medication_delete.html'


'''
CSV EXPORT
'''
def export_to_csv(queryset):
    '''
    Export to csv
    '''
    animal_resource = AnimalInstanceResource()
    dataset = animal_resource.export(queryset)
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="All_Animals.xls"'
    return response

def all_animal_export(request):
    queryset = AnimalInstance.objects.all()
    return export_to_csv(queryset)

def all_available_export(request):
    queryset = AnimalInstance.objects.filter(status__exact='a')
    return export_to_csv(queryset)

def all_quarantine_export(request):
    queryset = AnimalInstance.objects.filter(status__exact='q')
    return export_to_csv(queryset)

def all_adopted_export(request):
    queryset = AnimalInstance.objects.filter(status__exact='d')
    return export_to_csv(queryset)

def all_reserved_export(request):
    animal_resource = AnimalInstanceResource()
    return export_to_csv(queryset)
