from django.db import models


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
    type = models.CharField(max_length = 30, null= False, blank= False, help_text= 'What color(s) is the animal?')

    def __str__(self):
        return self.type
        
class Animal(models.Model):
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
    animal_species = models.CharField(max_length= 30, null= False, blank= True, help_text= 'Please choose what species of animal this is.')
    join_date= models.DateField(null=False, blank=False, help_text= 'Date animal started at the shelter.')
    gender= models.CharField(blank= True, choices= GENDER_CHOICES)
    breed = models.CharField(max_length= 40, help_text= 'Please select what breed of animal it is.')
    hair_type = models.CharField(max_length= 1, choices = HAIR_TYPE_CHOICES, help_text= 'Please select the type of hair it has.')
    hair_length = models.CharField(max_length= 1, choices= HAIR_LENGTH_CHOICES, help_text= 'Please select the length of the hair.')
    color = models.ManyToManyField(Color, max_length= 1, help_text= 'Confirm which colour(s) the animal is.')
    
    def __str__(self):
        return '{0} {1}'.format(self.color, self.animal_species)

class AnimalInstance(models.Model):
    ADOPTION_STATUS = (
        ('a','Available'),
        ('q','Quarantine'),
        ('r','Reserved'),
        ('d','Adopted'),
    )

    status= models.CharField(max_length=1, help_text= 'Please select the status of the animal.')
    name = models.CharField(max_length= 30, null= False, blank= False, help_text= 'The name of the animal.')
    species = models.ForeignKey('Animal', on_delete=models.PROTECT)
    cross = models.NullBooleanField(blank= True)
    bio = models.TextField(max_length = 1000, help_text= 'Enter a breif description about the animal. \
                                                         \nThis may include distinctive markings, additional behaviour or care comments.')
    personality= models.TextField(max_length= 200, null= False, blank= True, help_text='Summarise the animal\'s demeanour\ne.g. calm, friendly')
    status= models.CharField(max_length= 1, choices=ADOPTION_STATUS, help_text='Select the best fit status for the animal.')
    
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
    name = models.CharField('Building Name', help_text= 'Please enter the name of the shelter building.')

class Home_History(Address):
    current = models.NullBooleanField(blank= True)

class Caretakers(Address):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length= 30)
    email = models.EmailField(message='Please enter a valid email address', blank=True)
    contactnumber1 = models.IntegerField(help_text= 'The primary contact number.')
    contactnumber2 = models.IntegerField(help_text= 'The secondary contact number.')
    animal = models.ForeignKey('Animal', on_delete=models.PROTECT)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

class Medication(models.Model):
    TYPE_CHOICES = (
        ('p', 'Pill'),
        ('i', 'Injection'),
    )
    name = models.CharField('Medication')
    type = models.CharField(choices=TYPE_CHOICES)
    date_start = models.DateField()
    date_finish = models.DateField()
    weekly_dose = models.CharField(help_text= 'How many days in the week need medication \
                                                e.g. 3 times a day every day would mean this is 7- a dose required each day.')
    daily_dose = models.CharField(help_text = 'How many times per day.')
