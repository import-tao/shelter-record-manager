from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

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
    # These tuples are formed part of the model below and referenced by choices = **
    # the first part (a) is the 'backend' part and therefore what is stored in the database,
    # whereas the second part (Available) is the frontend part what the user will see
    ADOPTION_STATUS = (
        ('a','Available'),
        ('q','Quarantine'),
        ('r','Reserved'),
        ('d','Adopted'),
    )
    HAIR_TYPE_CHOICES = (
        ('f','Flat'),
        ('c','Curly'),
        ('w','Wiry'),
        ('f','Fluffy'),
        ('s','Smooth'),
    )
    HAIR_LENGTH_CHOICES = (
        ('l','Long'),
        ('s','Short'),
        ('m','Medium'),
        ('h','Hairless'),
    )
    GENDER_CHOICES = (
        ('m','Male'),
        ('f','Female'),
    )
    FOOD_TYPE_CHOICES = (
        ('h','Hard'),
        ('s','Soft'),
    )
    animal_species = models.CharField(max_length= 30, null= False, blank= True, help_text= 'What species of animal.')
    breed = models.CharField(max_length= 40, help_text= 'What breed of animal it is.', blank=True)
    name = models.CharField(max_length= 30, null= False, blank= False, help_text= 'The name of the animal.')
    # For foreign keys, if the table is before it, you do not have to put it in a string, but if it is after you do, otherwise it will result in an error.
    # New in 2.0 the on_delete became mandatory. This defines what happens when the other table dets deleted and there are various options of nulling the field
    # deleting it as well (CASCADE), stopping it from being deleted (PROTECT). More information is within the django docs.
    cross = models.NullBooleanField(blank= True, default= False, help_text = 'Is the animal a cross breed? if not sure select No.')
    bio = models.TextField(max_length = 1000, help_text= 'Enter a brief description about the animal and their personality. \
                                                         This may include distinctive markings, \
                                                        additional behaviour or care comments.')
    status= models.CharField(max_length= 1, choices=ADOPTION_STATUS, help_text='Select the best fit status for the animal.')
    arrival_date= models.DateField(null=False, blank=False, help_text= 'Date animal started at the shelter.', default=timezone.now)
    leaving_date = models.DateField(null=True, blank=True, help_text= 'Date animal left the shelter.')
    gender= models.CharField(max_length= 6, blank= False, choices= GENDER_CHOICES, default='f')
    hair_type = models.CharField(max_length= 1, choices = HAIR_TYPE_CHOICES, help_text= 'Please select the type of hair it has.', blank= True)
    hair_length = models.CharField(max_length= 1, choices= HAIR_LENGTH_CHOICES, help_text= 'Please select the length of the hair.', default = 's', blank= True)
    cage = models.ForeignKey('Building', on_delete= models.CASCADE, blank = True, null=True)
    adopter_first_name = models.CharField('First Name', max_length = 30, blank=True)
    adopter_last_name = models.CharField('Last Name', max_length= 30, blank= True)
    adopter_email = models.EmailField('Email', help_text='Please enter a valid email address', blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    adopter_contactnumber1 = models.CharField('Primary Contact Number', validators=[phone_regex], max_length=17, blank=True, default= 0000)
    adopter_contactnumber2 = models.CharField('Secondary Contact Number', validators=[phone_regex], max_length=17, blank=True, default=0000)
    food_type = models.CharField(max_length=1, choices=FOOD_TYPE_CHOICES, blank=True)
    portion_size = models.FloatField(help_text= 'How big is each portion of food in lbs?', blank=True, default = 1)
    daily_portions = models.FloatField('Meals per day', help_text='How many meals per day?', blank= True, default = 1)
    allergies = models.ManyToManyField('Allergies', help_text='Ctrl+click to select multiple/deselect', blank=True)
    medication = models.ManyToManyField('Medication', blank=True)
    medication_date_start = models.DateField('Date Medication Started', blank=True, null=True)
    medication_date_finish = models.DateField('End Date', blank=True, null=True)
    medication_weekly_dose = models.IntegerField('Weekly Dose', help_text= 'How many days in the week need medication \
                                                e.g. 3 times a day every day would mean this is 7- a dose required each day.', blank=True, null=True)
    medication_daily_dose = models.IntegerField('Daily Dose', help_text = 'How many times per day.', blank=True, null=True)

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.animal_species)

    # get_absolute_url will create an automatic url hyperlink for this class and in the admin site, it will have an option 'VIEW ON SITE' which will go direct to it
    # this is also useful when writing navigation within the front end to easily hyperlink to an Animal.
    # pk = primary key. These are automatically created by django in their own field. You can create your own if you
    # wish by using an UUID - More info about UUID in the Mozilla django guide
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("animal_detail", args=[str(self.id)])

    def get_update_url(self):
        from django.urls import reverse
        return reverse('animal_instance_update', args=[str(self.id)])

    def get_delete_url(self):
        from django.urls import reverse
        return reverse('animal_instance_delete', args=[str(self.id)])

    def get_adopt_url(self):
        from django.urls import reverse
        return reverse('adopt_new', args=[str(self.id)])

    def update_adopted_url(self):
        from django.urls import reverse
        return reverse('adopt_existing', args=[str(self.id)])

class Building(models.Model):
    room= models.CharField(max_length= 20, blank= False)
    cage= models.CharField(max_length= 10, blank= False)

    def __str__(self):
        return 'Cage {} in {}'.format(self.cage, self.room)

    def get_cage_url(self):
        from django.urls import reverse
        return reverse("cage_update", args=[str(self.id)])

    def get_cage_delete_url(self):
        from django.urls import reverse
        return reverse('cage_delete', args=[str(self.id)])

    class Meta:
        ordering = ['-room', 'cage']


class Address(models.Model):
    number_or_name = models.CharField(max_length= 20, help_text= 'Please enter the house number or name.')
    street = models.CharField(max_length = 30, help_text= 'Street name')
    city = models.CharField(max_length = 30)
    province = models.CharField(max_length= 30)
    code = models.CharField(max_length=15, help_text='Please enter the ZIP code / postcode.')
    date_from = models.DateField(null=True, blank= True)
    date_to = models.DateField(null=True, blank= True)

    # Using abstract means that this class/model doesnt actually get stored so to speak, but is instead used to inheret into other models. This is to avoid repetition
    # To inheret you use this class name instead of models.Model as seen in the Shelter_Location class below
    class Meta:
        abstract= True

class Shelter_Location(Address):
    name = models.CharField('Building Name', max_length = 40, help_text= 'Please enter the name of the shelter building.')
    rooms = models.ForeignKey(Building, on_delete= models.CASCADE)

    def __str__(self):
        return '{}, {}'.format(self.name, self.street)

    class Meta:
        verbose_name = 'Shelter Location'
        verbose_name_plural = 'Shelter Locations'


class Medication(models.Model):
    TYPE_CHOICES = (
        ('p', 'Pill'),
        ('i', 'Injection'),
        ('c', 'Cream'),
        ('d', 'Drops'),
    )
    name = models.CharField('Medication', max_length= 50)
    type1 = models.CharField('Type', max_length= 1, choices=TYPE_CHOICES)

    def __str__(self):
        return '{}, {}'.format(self.name, self.type1)

    def get_delete_url(self):
        from django.urls import reverse
        return reverse("medication_delete", args=[str(self.id)])

class Allergies(models.Model):
    allergy = models.CharField(max_length= 35, blank=True, null=True)
    def __str__(self):
        return self.allergy

    class Meta:
        ordering = ('allergy',)
        verbose_name_plural = 'Allergies'

    def get_delete_url(self):
        from django.urls import reverse
        return reverse("allergy_delete", args=[str(self.id)])
