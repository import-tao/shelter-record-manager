from django.db import models
from django.utils import timezone

# Create your models here.
'''
To do 
- details about each animal themselves e.g. name, dob etc
- the species 
- the location
- caretakers
- home history
- medical needs
- dietary needs
'''
class Color(models.Model):
    colorfield = models.CharField('Color', max_length = 30, null= False, blank= False, help_text= 'What color(s) is the animal?', default='Black')

    def __str__(self):
        return self.colorfield
    
    class Meta:
        ordering = ('colorfield',)
        
class Animal(models.Model):
    animal_species = models.CharField(max_length= 30, null= False, blank= True, help_text= 'Please choose what species of animal this is.')
    color = models.ManyToManyField(Color, help_text= 'Confirm which colour(s) the animal is.')
    breed = models.CharField(max_length= 40, help_text= 'Please select what breed of animal it is.')    

    def __str__(self):
        return '{0} {1}'.format(", ".join([col.colorfield for col in self.color.all()]), self.animal_species)

class AnimalInstance(models.Model):
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

    status= models.CharField(max_length=1, help_text= 'Please select the status of the animal.')
    name = models.CharField(max_length= 30, null= False, blank= False, help_text= 'The name of the animal.')
    species = models.ForeignKey('Animal', on_delete=models.PROTECT)
    cross = models.NullBooleanField(blank= True, default= False, help_text = 'Is the animal a cross breed? if not sure select No.')
    bio = models.TextField(max_length = 1000, help_text= 'Enter a brief description about the animal. \
                                                         \nThis may include distinctive markings, \
                                                        additional behaviour or care comments.')
    personality= models.TextField(max_length= 200, null= False, blank= True, \
                                    help_text='Summarise the animal\'s demeanour\ne.g. calm, friendly')
    status= models.CharField(max_length= 1, choices=ADOPTION_STATUS, help_text='Select the best fit status for the animal.')
    join_date= models.DateField(null=False, blank=False, help_text= 'Date animal started at the shelter.', default=timezone.now)
    gender= models.CharField(max_length= 6, blank= False, choices= GENDER_CHOICES, default='f')
    hair_type = models.CharField(max_length= 1, choices = HAIR_TYPE_CHOICES, help_text= 'Please select the type of hair it has.', default= 'f')
    hair_length = models.CharField(max_length= 1, choices= HAIR_LENGTH_CHOICES, help_text= 'Please select the length of the hair.', default = 's')
    caretaker = models.ForeignKey('Caretakers', on_delete=models.CASCADE, blank = True)
    homehistory = models.ForeignKey('Home_History', on_delete= models.CASCADE, blank= True)
    diet = models.ForeignKey('Diet', on_delete = models.CASCADE, blank = True)
    medication = models.ForeignKey('Medication', on_delete = models.CASCADE, blank= True)
    allergies = models.ForeignKey('Allergies',on_delete = models.CASCADE, blank= True)

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.species)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("animal_detail", kwargs={"pk": self.pk})

class Building(models.Model):
    facility = models.ForeignKey('Shelter_Location', on_delete=models.PROTECT, blank=False)
    room= models.CharField(max_length= 20, blank= True)
    cage= models.CharField(max_length= 10, blank=False)

class Address(models.Model):
    number_or_name = models.CharField(max_length= 20, help_text= 'Please enter the house number or name.')
    street = models.CharField(max_length = 30, help_text= 'Please enter the full address excluding ZIP Code/Postcode.')
    city = models.CharField(max_length = 30)
    province = models.CharField(max_length= 30)
    code = models.CharField(max_length=15, help_text='Please enter the ZIP code / postcode.')
    date_from = models.DateField(null=False, blank= True)
    date_to = models.DateField(null=False, blank= True)

    class Meta:
        abstract= True 

class Shelter_Location(Address):
    name = models.CharField('Building Name', max_length = 40, help_text= 'Please enter the name of the shelter building.')
    site = models.ForeignKey(Building, on_delete= models.CASCADE)

    class Meta:
        verbose_name = 'Shelter Location'
        verbose_name_plural = 'Shelter Locations'

class Home_History(Address):
    current = models.NullBooleanField('Current Address?', blank= True)

    class Meta:
        verbose_name = 'Home history'
        verbose_name_plural = 'Home history'

class Caretakers(Address):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length= 30)
    email = models.EmailField(help_text='Please enter a valid email address', blank=True)
    contactnumber1 = models.IntegerField(help_text= 'The primary contact number.')
    contactnumber2 = models.IntegerField(help_text= 'The secondary contact number.')

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
    
    class Meta:
        verbose_name_plural = 'Caretakers'

class Medication(models.Model):
    TYPE_CHOICES = (
        ('p', 'Pill'),
        ('i', 'Injection'),
        ('c', 'Cream'),
        ('d', 'Drops'),
    )
    comment1 = models.TextField(max_length = 200, help_text='Please provide more information.', default='')
    name = models.CharField('Medication', max_length= 50)
    type1 = models.CharField('Type', max_length= 1,choices=TYPE_CHOICES)
    date_start = models.DateField()
    date_finish = models.DateField()
    weekly_dose = models.IntegerField(help_text= 'How many days in the week need medication \
                                                e.g. 3 times a day every day would mean this is 7- a dose required each day.')
    daily_dose = models.IntegerField(help_text = 'How many times per day.')

class Allergies(models.Model):
    allergy = models.CharField(max_length= 35, help_text = 'What allergies does the animal have?')

    def __str__(self):
        return self.allergy
    
    class Meta:
        ordering = ('allergy',)
        verbose_name_plural = 'Allergies'

class Diet(models.Model):
    FOOD_TYPE_CHOICES = (
        ('h','Hard'),
        ('s','Soft'),
    )
    comment2 = models.TextField(max_length=200, help_text = 'Further comments.', default="")
    food_type = models.CharField(max_length=1, choices=FOOD_TYPE_CHOICES)
    portion_size = models.IntegerField(help_text= 'How big is each portion of food in lbs?')
    daily_portions = models.IntegerField('Meals per day', help_text='How many meals per day?')
    allergy = models.ManyToManyField(Allergies, help_text = 'What allergies (if any?) does the animal have?')

    def __str__(self):
        return '{0} food, {1}lbs {2} times a day'.format(self.food_type, self.portion_size, self.daily_portions)
    
    class Meta:
        ordering = ('food_type',)
        verbose_name_plural = 'Diet'
