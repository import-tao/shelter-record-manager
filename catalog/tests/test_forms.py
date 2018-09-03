from django.test import TestCase
from django.utils import timezone
from catalog.forms import AnimalInstanceCreateForm, AnimalInstanceAdoptForm, AdopterDetailsForm, BuildingCreateForm, MedicationCreateForm, AllergiesCreateForm

class AnimalCreateForm(TestCase):
    def test_valid_sign_up(self):
        form = AnimalInstanceCreateForm(data = {
            'animal_species':'Dog',
            'breed':'Labrador',
            'name':'Dexter',
            'bio':'Funny Dogo',
            'status':'a',
            'arrival_date':timezone.now(),
            'gender':'m',
            'hair_type':'f',
            'hair_length':'s',
        })
        return self.assertTrue(form.is_valid())