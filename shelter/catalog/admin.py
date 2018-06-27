from django.contrib import admin
from .models import Animal, Allergies, Animal, AnimalInstance, Building, Caretakers, Diet, Home_History, Medication, Shelter_Location, Color

# Register your models here.

admin.site.register(Animal)
admin.site.register(AnimalInstance)
admin.site.register(Allergies)
admin.site.register(Building)
admin.site.register(Caretakers)
admin.site.register(Color)
admin.site.register(Diet)
admin.site.register(Home_History)
admin.site.register(Medication)
admin.site.register(Shelter_Location)