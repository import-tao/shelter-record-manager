from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import timedelta
from catalog.models import Building, AnimalInstance, Allergies, Medication, Shelter_Location

class AnimalInstanceLabellTest(TestCase):
    def setUp(self):
        build = Building.objects.create(
           room = 'Main',
           cage = 1,
        )

        current_date = timezone.now()
        AnimalInstance.objects.create(
            name = 'Dexter',
            animal_species = 'Dog',
            breed = 'Labrador',
            cross = False,
            status = 'a',
            arrival_date = current_date,
            leaving_date = current_date + timedelta(weeks=1),
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
        
        current_date = timezone.now()
        AnimalInstance.objects.create(
            name = 'Dexter',
            animal_species = 'Dog',
            breed = 'Labrador',
            cross = False,
            status = 'a',
            arrival_date = current_date,
            leaving_date = current_date + timedelta(weeks=1),
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
        
        current_date = timezone.now()
        AnimalInstance.objects.create(
            name = 'Dexter',
            animal_species = 'Dog',
            breed = 'Labrador',
            cross = False,
            status = 'a',
            arrival_date = current_date,
            leaving_date = current_date + timedelta(weeks=1),
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

class AnimalInstanceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.building = Building.objects.create(
            room='Main',
            cage=1,
        )
        
        current_date = timezone.now()
        cls.animal = AnimalInstance.objects.create(
            name='Dexter',
            animal_species='Dog',
            breed='Labrador',
            cross=False,
            status='a',
            arrival_date=current_date,
            gender='m',
            cage=cls.building,
        )

    def test_name_max_length(self):
        animal = AnimalInstance.objects.get(id=1)
        max_length = animal._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_animal_species_max_length(self):
        animal = AnimalInstance.objects.get(id=1)
        max_length = animal._meta.get_field('animal_species').max_length
        self.assertEqual(max_length, 200)

    def test_breed_max_length(self):
        animal = AnimalInstance.objects.get(id=1)
        max_length = animal._meta.get_field('breed').max_length
        self.assertEqual(max_length, 200)

    def test_status_choices(self):
        animal = AnimalInstance.objects.get(id=1)
        status_choices = dict(animal._meta.get_field('status').choices)
        self.assertEqual(set(status_choices.keys()), {'a', 'r', 'q', 'd'})

    def test_gender_choices(self):
        animal = AnimalInstance.objects.get(id=1)
        gender_choices = dict(animal._meta.get_field('gender').choices)
        self.assertEqual(set(gender_choices.keys()), {'m', 'f'})

    def test_invalid_future_arrival_date(self):
        animal = AnimalInstance.objects.get(id=1)
        future_date = timezone.now() + timedelta(days=1)
        animal.arrival_date = future_date
        with self.assertRaises(ValidationError):
            animal.full_clean()

    def test_invalid_leaving_date_before_arrival(self):
        animal = AnimalInstance.objects.get(id=1)
        current_date = timezone.now()
        animal.arrival_date = current_date
        animal.leaving_date = current_date - timedelta(days=1)
        with self.assertRaises(ValidationError):
            animal.full_clean()

    def test_str_representation(self):
        animal = AnimalInstance.objects.get(id=1)
        expected_str = f'{animal.name}, {animal.animal_species}'
        self.assertEqual(str(animal), expected_str)

    def test_get_absolute_url(self):
        animal = AnimalInstance.objects.get(id=1)
        self.assertEqual(animal.get_absolute_url(), reverse('animal_detail', args=[str(animal.id)]))

class BuildingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.building = Building.objects.create(
            room='Main',
            cage=1,
        )

    def test_room_max_length(self):
        building = Building.objects.get(id=1)
        max_length = building._meta.get_field('room').max_length
        self.assertEqual(max_length, 200)

    def test_cage_positive(self):
        building = Building.objects.get(id=1)
        building.cage = -1
        with self.assertRaises(ValidationError):
            building.full_clean()

    def test_str_representation(self):
        building = Building.objects.get(id=1)
        expected_str = f'Cage {building.cage} in {building.room}'
        self.assertEqual(str(building), expected_str)

    def test_get_cage_url(self):
        building = Building.objects.get(id=1)
        self.assertEqual(building.get_cage_url(), reverse('cage_update', args=[str(building.id)]))

class AllergiesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.allergy = Allergies.objects.create(
            allergy='Wheat'
        )

    def test_allergy_max_length(self):
        allergy = Allergies.objects.get(id=1)
        max_length = allergy._meta.get_field('allergy').max_length
        self.assertEqual(max_length, 200)

    def test_str_representation(self):
        allergy = Allergies.objects.get(id=1)
        self.assertEqual(str(allergy), allergy.allergy)

    def test_get_delete_url(self):
        allergy = Allergies.objects.get(id=1)
        self.assertEqual(allergy.get_delete_url(), reverse('allergy_delete', args=[str(allergy.id)]))

class MedicationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.medication = Medication.objects.create(
            name='Paracetamol',
            type1='p',
        )

    def test_name_max_length(self):
        medication = Medication.objects.get(id=1)
        max_length = medication._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_type1_choices(self):
        medication = Medication.objects.get(id=1)
        type_choices = dict(medication._meta.get_field('type1').choices)
        self.assertEqual(set(type_choices.keys()), {'p', 'l', 't', 'i'})

    def test_str_representation(self):
        medication = Medication.objects.get(id=1)
        expected_str = f'{medication.name}, {medication.type1}'
        self.assertEqual(str(medication), expected_str)

    def test_get_delete_url(self):
        medication = Medication.objects.get(id=1)
        self.assertEqual(medication.get_delete_url(), reverse('medication_delete', args=[str(medication.id)]))