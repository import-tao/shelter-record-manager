from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from datetime import timedelta
from catalog.models import Building, AnimalInstance, Allergies, Medication, Shelter_Location

class AnimalInstanceLabellTest(TestCase):
    def setUp(self):
        build = Building.objects.create(
           room = 'Main',
           cage = 1,
        )

        AnimalInstance.objects.create(
            name = 'Dexter',
            animal_species = 'Dog',
            breed = 'Labrador',
            cross = False,
            status = 'a',
            arrival_date = datetime.now().date(),
            leaving_date = datetime.now().date() + timedelta(weeks= 1),
            gender = 'Male',
            cage = build,
        )

        Allergies.objects.create(
            allergy = 'Wheat'
        )

        Medication.objects.create(
            name = 'Paracetamol',
            type1 = 'p'
        )
    
    
    def test_adopter_first_name_label(self):
        adopter = AnimalInstance.objects.get(id=1)
        field_label = adopter._meta.get_field('adopter_first_name').verbose_name
        self.assertEqual(field_label, 'First Name')
    
    def test_adopter_last_name_label(self):
        adopter = AnimalInstance.objects.get(id=1)
        field_label = adopter._meta.get_field('adopter_last_name').verbose_name
        self.assertEqual(field_label, 'Last Name')

    def test_adopter_email_label(self):
        adopter = AnimalInstance.objects.get(id=1)
        field_label = adopter._meta.get_field('adopter_email').verbose_name
        self.assertEqual(field_label, 'Email')

    def test_adopter_phone1_label(self):
        adopter = AnimalInstance.objects.get(id=1)
        field_label = adopter._meta.get_field('adopter_contactnumber1').verbose_name
        self.assertEqual(field_label, 'Primary Contact Number')

    def test_adopter_phone2_label(self):
        adopter = AnimalInstance.objects.get(id=1)
        field_label = adopter._meta.get_field('adopter_contactnumber2').verbose_name
        self.assertEqual(field_label, 'Secondary Contact Number')

    def test_meal_portions_label(self):
        adopter = AnimalInstance.objects.get(id=1)
        field_label = adopter._meta.get_field('daily_portions').verbose_name
        self.assertEqual(field_label, 'Meals per day')

    def test_medication_start_date_label(self):
        adopter = AnimalInstance.objects.get(id=1)
        field_label = adopter._meta.get_field('medication_date_start').verbose_name
        self.assertEqual(field_label, 'Date Medication Started')

    def test_medication_end_date_label(self):
        adopter = AnimalInstance.objects.get(id=1)
        field_label = adopter._meta.get_field('medication_date_finish').verbose_name
        self.assertEqual(field_label, 'End Date')

    def test_medication_weekly_dose_label(self):
        adopter = AnimalInstance.objects.get(id=1)
        field_label = adopter._meta.get_field('medication_weekly_dose').verbose_name
        self.assertEqual(field_label, 'Weekly Dose')

    def test_medication_daily_dose_label(self):
        adopter = AnimalInstance.objects.get(id=1)
        field_label = adopter._meta.get_field('medication_daily_dose').verbose_name
        self.assertEqual(field_label, 'Daily Dose')


class Str_Checks(TestCase):

    def setUp(self):
        build = Building.objects.create(
           room = 'Main',
           cage = 1,
        )
        
        AnimalInstance.objects.create(
            name = 'Dexter',
            animal_species = 'Dog',
            breed = 'Labrador',
            cross = False,
            status = 'a',
            arrival_date = datetime.now().date(),
            leaving_date = datetime.now().date() + timedelta(weeks= 1),
            gender = 'Male',
            cage = build,
        )

        Allergies.objects.create(
            allergy = 'Wheat'
        )

        Medication.objects.create(
            name = 'Paracetamol',
            type1 = 'p',
        )
    
    def test_animal_instance_str(self):
        animal = AnimalInstance.objects.get(id=1)
        expected_object_name = f'{animal.name}, {animal.animal_species}'
        self.assertEqual(expected_object_name, str(animal))
    
    def test_building_str(self):
        build = Building.objects.get(id=1)
        expected_object_name = f'Cage {build.cage} in {build.room}'
        self.assertEqual(expected_object_name , str(build))
    
    def test_medication_str(self):
        medi = Medication.objects.get(id=1)
        expected_object_name = f'{medi.name}, {medi.type1}'
        self.assertEqual(expected_object_name, str(medi))
    
    def test_allergies_str(self):
        allergy = Allergies.objects.get(id=1)
        expected_object_name = f'{allergy.allergy}'
        self.assertEqual(expected_object_name, str(allergy))


class AbsoluteUrlTests(TestCase):

    def setUp(self):
        build = Building.objects.create(
           room = 'Main',
           cage = 1,
        )
        
        AnimalInstance.objects.create(
            name = 'Dexter',
            animal_species = 'Dog',
            breed = 'Labrador',
            cross = False,
            status = 'a',
            arrival_date = datetime.now().date(),
            leaving_date = datetime.now().date() + timedelta(weeks= 1),
            gender = 'Male',
            cage = build,
        )

        Allergies.objects.create(
            allergy = 'Wheat'
        )

        Medication.objects.create(
            name = 'Paracetamol',
            type1 = 'p',
        )
    
    def test_animal_instance_absolute_url(self):
        animal = AnimalInstance.objects.get(id=1)
        self.assertEqual(animal.get_absolute_url(), reverse('animal_detail', args=[str(animal.id)]))
    
    def test_animal_instance_update_url(self):
        animal = AnimalInstance.objects.get(id=1)
        self.assertEqual(animal.get_update_url(), reverse('animal_instance_update', args=[str(animal.id)]))

    def test_animal_instance_delete_url(self):
        animal = AnimalInstance.objects.get(id=1)
        self.assertEqual(animal.get_delete_url(), reverse('animal_instance_delete', args=[str(animal.id)]))

    def test_animal_instance_adopt_url(self):
        animal = AnimalInstance.objects.get(id=1)
        self.assertEqual(animal.get_adopt_url(), reverse('adopt_new', args=[str(animal.id)]))

    def test_animal_instance_update_adopt_url(self):
        animal = AnimalInstance.objects.get(id=1)
        self.assertEqual(animal.update_adopted_url(), reverse('adopt_existing', args=[str(animal.id)]))

    def test_building_cage_url(self):
        build = Building.objects.get(id=1)
        self.assertEqual(build.get_cage_url(), reverse('cage_update', args=[str(build.id)]))

    def test_building_cage_delete_url(self):
        build = Building.objects.get(id=1)
        self.assertEqual(build.get_cage_delete_url(), reverse('cage_delete', args=[str(build.id)]))

    def test_medication_delete_url(self):
        medi = Medication.objects.get(id=1)
        self.assertEqual(medi.get_delete_url(), reverse("medication_delete", args=[str(medi.id)]))

    def test_allergies_delete_url(self):
        allergy = Allergies.objects.get(id=1)
        self.assertEqual(allergy.get_delete_url(), reverse("allergy_delete", args=[str(allergy.id)]))