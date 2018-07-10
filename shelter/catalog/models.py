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
# for the different type of model fields (manytomany, foreignkey, charfield, textfield, integerfield, flotfield etc. refer to the docs 
# https://docs.djangoproject.com/en/2.0/topics/db/models/ or the mozilla guide which i found very useful https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models
class Color(models.Model):
    colorfield = models.CharField('Color', max_length = 30, null= False, blank= False, help_text= 'What color(s) is the animal?')
    
    # str function returns what the object of this will be displayed as
    def __str__(self):
        return self.colorfield
    
    # Meta shows the high level information which can include:
    # the front end display name of the class, how the data is ordered when viewed in admin as well as how the plural of it
    class Meta:
        ordering = ('colorfield',)
        
class Animal(models.Model):
    animal_species = models.CharField(max_length= 30, null= False, blank= True, help_text= 'Please choose what species of animal this is.')
    color = models.ManyToManyField(Color, help_text= 'Confirm which colour(s) the animal is.', blank= True)
    breed = models.CharField(max_length= 40, help_text= 'Please select what breed of animal it is.', blank=True)    

    # This str function is different as it has a list comprehension. This is used because it is getting info from a many to many field and therefore
    # need to join up all the possible 'colours'.

    def __str__(self):
        return '{0} {1} {2}'.format(", ".join([col.colorfield for col in self.color.all()]), self.breed, self.animal_species)

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

    name = models.CharField(max_length= 30, null= False, blank= False, help_text= 'The name of the animal.')
    # For foreign keys, if the table is before it, you do not have to put it in a string, but if it is after you do, otherwise it will result in an error.
    # New in 2.0 the on_delete became mandatory. This defines what happens when the other table dets deleted and there are various options of nulling the field
    # deleting it as well (CASCADE), stopping it from being deleted (PROTECT). More information is within the django docs.
    species = models.ForeignKey('Animal', on_delete=models.PROTECT, blank=True, null=True)
    cross = models.NullBooleanField(blank= True, default= False, help_text = 'Is the animal a cross breed? if not sure select No.')
    bio = models.TextField(max_length = 1000, help_text= 'Enter a brief description about the animal and their personality. \
                                                         This may include distinctive markings, \
                                                        additional behaviour or care comments.')
    status= models.CharField(max_length= 1, choices=ADOPTION_STATUS, help_text='Select the best fit status for the animal.')
    join_date= models.DateField(null=False, blank=False, help_text= 'Date animal started at the shelter.', default=timezone.now)
    leaving_date = models.DateField(null=True, blank=True, help_text= 'Date animal left the shelter.')
    gender= models.CharField(max_length= 6, blank= False, choices= GENDER_CHOICES, default='f')
    hair_type = models.CharField(max_length= 1, choices = HAIR_TYPE_CHOICES, help_text= 'Please select the type of hair it has.', blank= True)
    hair_length = models.CharField(max_length= 1, choices= HAIR_LENGTH_CHOICES, help_text= 'Please select the length of the hair.', default = 's', blank= True)
    caretaker = models.ForeignKey('Caretakers', on_delete=models.CASCADE, blank = True, null=True)
    homehistory = models.ForeignKey('Home_History', on_delete= models.CASCADE, blank= True, null=True)
    diet = models.ForeignKey('Diet', on_delete = models.CASCADE, blank = True, null=True)
    medication = models.ForeignKey('Medication', on_delete = models.CASCADE, blank= True, null=True)
    allergies = models.ForeignKey('Allergies',on_delete = models.CASCADE, blank= True, null= True)

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.species)

    # get_absolute_url will create an automatic url hyperlink for this class and in the admin site, it will have an option 'VIEW ON SITE' which will go direct to it
    # this is also useful when writing navigation within the front end to easily hyperlink to an Animal.
    # pk = primary key. These are automatically created by django in their own field. You can create your own if you 
    # wish by using an UUID - More info about UUID in the Mozilla django guide
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("animal_detail", args=[self.name, str(self.id)])
    
    def get_update_url(self):
        from django.urls import reverse
        return reverse('animal_instance_update', args=[self.name, str(self.id)])
    
    def get_delete_url(self):
        from django.urls import reverse
        return reverse('animal_instance_delete', args=[self.name, str(self.id)])

class Building(models.Model):
    room= models.CharField(max_length= 20, blank= True)
    cage= models.CharField(max_length= 10, blank=False)

    def __str__(self):
        return 'Cage {} {}'.format(self.cage, self.room)

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

class Home_History(Address):

    def __str__(self):
        return '{}'.format(self.street)

    class Meta:
        verbose_name = 'Prior Address'
        verbose_name_plural = 'Prior Address'

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
    comment1 = models.TextField('Comments', max_length = 200, help_text='Please provide more information.', default='')
    name = models.CharField('Medication', max_length= 50)
    type1 = models.CharField('Type', max_length= 1, choices=TYPE_CHOICES)
    date_start = models.DateField()
    date_finish = models.DateField()
    weekly_dose = models.IntegerField(help_text= 'How many days in the week need medication \
                                                e.g. 3 times a day every day would mean this is 7- a dose required each day.')
    daily_dose = models.IntegerField(help_text = 'How many times per day.')

    def __str__(self):
        return '{}, {} times a day, {} a week'.format(self.name, self.daily_dose, self.weekly_dose)

class Allergies(models.Model):
    allergy = models.CharField(max_length= 35, help_text = 'What allergies does the animal have?', blank=True, null=True)

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
    comment2 = models.TextField('Comments', max_length=200, help_text = 'Further comments.', default="")
    food_type = models.CharField(max_length=1, choices=FOOD_TYPE_CHOICES)
    portion_size = models.FloatField(help_text= 'How big is each portion of food in lbs?')
    daily_portions = models.FloatField('Meals per day', help_text='How many meals per day?')
    allergy = models.ManyToManyField(Allergies, help_text = 'What allergies (if any?) does the animal have?', blank=True)


    # To get choices in __str__ use self.get_*field name*_display() otherwise it will display the backend part (e.g. 'h' and not 'hard')
    def __str__(self):
        return '{0} food, {1}lbs {2} times a day'.format(self.get_food_type_display(), self.portion_size, self.daily_portions)
    
    # Django does have some logic for plurals but really it it just adds an s on the end. For most it is fine but
    # not always which is why it is defined here (verbose_name_plural = 'Diet') otherewise it would show as 
    # 'Diets' within admin
    class Meta:
        ordering = ('food_type',)
        verbose_name_plural = 'Diet'
