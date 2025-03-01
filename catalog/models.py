from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, MinValueValidator
from django.urls import reverse

# Create your models here.
'''
To do
- details about each animal themselves e.g. name, dob etc
- the species
- the location
- home history
- medical needs
- dietary needs
'''
# for the different type of model fields (manytomany, foreignkey, charfield, textfield, integerfield, flotfield etc. refer to the docs
# https://docs.djangoproject.com/en/2.0/topics/db/models/ or the mozilla guide which i found very useful https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models


class AnimalInstance(models.Model):
    class AdoptionStatus(models.TextChoices):
        AVAILABLE = 'a', 'Available'
        QUARANTINE = 'q', 'Quarantine'
        RESERVED = 'r', 'Reserved'
        ADOPTED = 'd', 'Adopted'

    class HairType(models.TextChoices):
        FLAT = 'f', 'Flat'
        CURLY = 'c', 'Curly'
        WIRY = 'w', 'Wiry'
        FLUFFY = 'l', 'Fluffy'
        SMOOTH = 's', 'Smooth'

    class HairLength(models.TextChoices):
        LONG = 'l', 'Long'
        SHORT = 's', 'Short'
        MEDIUM = 'm', 'Medium'
        HAIRLESS = 'h', 'Hairless'

    class Gender(models.TextChoices):
        MALE = 'm', 'Male'
        FEMALE = 'f', 'Female'

    class FoodType(models.TextChoices):
        HARD = 'h', 'Hard'
        SOFT = 's', 'Soft'

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    animal_species = models.CharField(
        max_length=200,
        blank=True,
        help_text='What species of animal.'
    )
    breed = models.CharField(
        max_length=200,
        help_text='What breed of animal it is.',
        blank=True
    )
    name = models.CharField(
        max_length=200,
        help_text='The name of the animal.'
    )
    cross = models.BooleanField(
        blank=True,
        default=False,
        help_text='Is the animal a cross breed? if not sure select No.'
    )
    bio = models.TextField(
        max_length=1000,
        help_text='Enter a brief description about the animal and their personality. '
                'This may include distinctive markings, additional behaviour or care comments.'
    )
    status = models.CharField(
        max_length=1,
        choices=AdoptionStatus.choices,
        help_text='Select the best fit status for the animal.'
    )
    arrival_date = models.DateTimeField(
        help_text='Date animal started at the shelter.',
        default=timezone.now
    )
    leaving_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text='Date animal left the shelter.',
        default=timezone.now
    )
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.FEMALE
    )
    hair_type = models.CharField(
        max_length=1,
        choices=HairType.choices,
        help_text='Please select the type of hair it has.',
        blank=True
    )
    hair_length = models.CharField(
        max_length=1,
        choices=HairLength.choices,
        default=HairLength.SHORT,
        blank=True
    )
    cage = models.ForeignKey(
        'Building',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    adopter_first_name = models.CharField(
        'First Name',
        max_length=30,
        blank=True
    )
    adopter_last_name = models.CharField(
        'Last Name',
        max_length=30,
        blank=True
    )
    adopter_email = models.EmailField(
        'Email',
        help_text='Please enter a valid email address',
        blank=True
    )
    phone_regex = RegexValidator(
        regex=r'^\d{10,11}$',
        message="Phone number must be 10 or 11 digits."
    )
    adopter_contactnumber1 = models.CharField(
        'Primary Contact Number',
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True
    )
    adopter_contactnumber2 = models.CharField(
        'Secondary Contact Number',
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True
    )
    food_type = models.CharField(
        max_length=1,
        choices=FoodType.choices,
        blank=True
    )
    portion_size = models.FloatField(
        help_text='How big is each portion of food in lbs?',
        blank=True,
        default=1
    )
    daily_portions = models.FloatField(
        'Meals per day',
        help_text='How many meals per day?',
        blank=True,
        default=1
    )
    allergies = models.ManyToManyField(
        'Allergies',
        help_text='Ctrl+click to select multiple/deselect',
        blank=True
    )
    medication = models.ManyToManyField('Medication', blank=True)
    medication_date_start = models.DateField(
        'Date Medication Started',
        blank=True,
        null=True
    )
    medication_date_finish = models.DateField(
        'End Date',
        blank=True,
        null=True
    )
    medication_weekly_dose = models.IntegerField(
        'Weekly Dose',
        help_text='How many days in the week need medication '
                'e.g. 3 times a day every day would mean this is 7- a dose required each day.',
        blank=True,
        null=True
    )
    medication_daily_dose = models.IntegerField(
        'Daily Dose',
        help_text='How many times per day.',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-date_added']
        indexes = [
            models.Index(fields=['name', 'animal_species']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return f'{self.name}, {self.animal_species}'

    def get_absolute_url(self):
        return reverse('animal_detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('animal_instance_update', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('animal_instance_delete', args=[str(self.id)])

    def get_adopt_url(self):
        return reverse('adopt_new', args=[str(self.id)])

    def update_adopted_url(self):
        return reverse('adopt_existing', args=[str(self.id)])

class Building(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    room = models.CharField(max_length=200, help_text='Enter room name')
    cage = models.PositiveIntegerField(help_text='Enter cage number', validators=[MinValueValidator(1)])

    class Meta:
        ordering = ['-room', 'cage']
        indexes = [
            models.Index(fields=['room', 'cage']),
        ]

    def __str__(self):
        return f'Cage {self.cage} in {self.room}'

    def get_cage_url(self):
        return reverse('cage_update', args=[str(self.id)])

    def get_cage_delete_url(self):
        return reverse('cage_delete', args=[str(self.id)])

class Address(models.Model):
    number_or_name = models.CharField(
        max_length=20,
        help_text='Please enter the house number or name.'
    )
    street = models.CharField(
        max_length=30,
        help_text='Street name'
    )
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    code = models.CharField(
        max_length=15,
        help_text='Please enter the ZIP code / postcode.'
    )
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True

class Shelter_Location(Address):
    name = models.CharField(
        'Building Name',
        max_length=40,
        help_text='Please enter the name of the shelter building.'
    )
    rooms = models.ForeignKey(Building, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Shelter Location'
        verbose_name_plural = 'Shelter Locations'
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f'{self.name}, {self.street}'

class Medication(models.Model):
    TYPE_CHOICES = [
        ('p', 'Pill'),
        ('l', 'Liquid'),
        ('t', 'Tablet'),
        ('i', 'Injection'),
    ]
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, help_text='Enter medication name')
    type1 = models.CharField(max_length=1, choices=TYPE_CHOICES, help_text='Select medication type')

    class Meta:
        indexes = [
            models.Index(fields=['name', 'type1']),
        ]

    def __str__(self):
        return f"{self.name}, {self.type1}"

    def get_delete_url(self):
        return reverse('medication_delete', args=[str(self.id)])

class Allergies(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    allergy = models.CharField(max_length=200, help_text='Enter allergy name')

    class Meta:
        ordering = ('allergy',)
        verbose_name_plural = 'Allergies'
        indexes = [
            models.Index(fields=['allergy']),
        ]

    def __str__(self):
        return self.allergy

    def get_delete_url(self):
        return reverse('allergy_delete', args=[str(self.id)])
