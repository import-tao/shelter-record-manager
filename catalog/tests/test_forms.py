from django.test import TestCase
from django.utils import timezone
from catalog.forms import (
    AnimalInstanceCreateForm, 
    AnimalInstanceAdoptForm, 
    BuildingCreateForm, 
    MedicationCreateForm, 
    AllergiesCreateForm
)

class AnimalCreateFormTest(TestCase):
    def test_valid_animal_creation(self):
        current_date = timezone.now()
        form_data = {
            'animal_species': 'Dog',
            'breed': 'Labrador',
            'name': 'Dexter',
            'bio': 'Friendly dog',
            'status': 'a',
            'arrival_date': current_date,
            'gender': 'm',
            'hair_type': 'f',
            'hair_length': 's',
        }
        form = AnimalInstanceCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_animal_creation_missing_required(self):
        form_data = {
            'bio': 'Friendly dog',  # Only optional field
        }
        form = AnimalInstanceCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 8)  # 8 required fields missing

    def test_invalid_animal_creation_future_arrival(self):
        future_date = timezone.now() + timezone.timedelta(days=1)
        form_data = {
            'animal_species': 'Dog',
            'breed': 'Labrador',
            'name': 'Dexter',
            'bio': 'Friendly dog',
            'status': 'a',
            'arrival_date': future_date,
            'gender': 'm',
            'hair_type': 'f',
            'hair_length': 's',
        }
        form = AnimalInstanceCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('arrival_date', form.errors)

class AnimalAdoptFormTest(TestCase):
    def test_valid_adoption(self):
        current_date = timezone.now()
        form_data = {
            'status': 'd',
            'leaving_date': current_date,
            'adopter_first_name': 'John',
            'adopter_last_name': 'Doe',
            'adopter_email': 'john@example.com',
            'adopter_contactnumber1': '1234567890',
        }
        form = AnimalInstanceAdoptForm(data=form_data)
        if not form.is_valid():
            print(form.errors)  # Debug output
        self.assertTrue(form.is_valid())

    def test_invalid_adoption_missing_required(self):
        form_data = {
            'status': 'd',
        }
        form = AnimalInstanceAdoptForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('leaving_date', form.errors)
        self.assertIn('adopter_first_name', form.errors)
        self.assertIn('adopter_last_name', form.errors)
        self.assertIn('adopter_email', form.errors)
        self.assertIn('adopter_contactnumber1', form.errors)

    def test_invalid_adoption_future_leaving_date(self):
        future_date = timezone.now() + timezone.timedelta(days=1)
        form_data = {
            'status': 'd',
            'leaving_date': future_date,
            'adopter_first_name': 'John',
            'adopter_last_name': 'Doe',
            'adopter_email': 'john@example.com',
            'adopter_contactnumber1': '1234567890',
        }
        form = AnimalInstanceAdoptForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('leaving_date', form.errors)

class BuildingCreateFormTest(TestCase):
    def test_valid_building_creation(self):
        form_data = {
            'room': 'Main Hall',
            'cage': 1,
        }
        form = BuildingCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_building_creation_missing_required(self):
        form_data = {}
        form = BuildingCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('room', form.errors)
        self.assertIn('cage', form.errors)

    def test_invalid_building_creation_negative_cage(self):
        form_data = {
            'room': 'Main Hall',
            'cage': -1,
        }
        form = BuildingCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('cage', form.errors)

class MedicationCreateFormTest(TestCase):
    def test_valid_medication_creation(self):
        form_data = {
            'name': 'Paracetamol',
            'type1': 'p',
        }
        form = MedicationCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_medication_creation_missing_required(self):
        form_data = {}
        form = MedicationCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('type1', form.errors)

class AllergiesCreateFormTest(TestCase):
    def test_valid_allergy_creation(self):
        form_data = {
            'allergy': 'Wheat',
        }
        form = AllergiesCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_allergy_creation_missing_required(self):
        form_data = {}
        form = AllergiesCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('allergy', form.errors)