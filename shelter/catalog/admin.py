from django.contrib import admin
from .models import Animal, Allergies, Animal, AnimalInstance, Building, Caretakers, Diet, Home_History, Medication, Shelter_Location, Color

# Register your models here.
# These is the basic way of registering the models to the admin site, make sure you import them above
admin.site.register(Animal)
admin.site.register(Allergies)
admin.site.register(Building)
admin.site.register(Caretakers)
admin.site.register(Color)
admin.site.register(Diet)
admin.site.register(Home_History)
admin.site.register(Medication)
admin.site.register(Shelter_Location)

# The decorator is one way of assigning the model to the class. 
# At the momment this class allows there to be a filter in the admin site by date and status which is handy when there is a lot of animals.
@admin.register(AnimalInstance)
class AnimalInstanceAdmin(admin.ModelAdmin):
    list_filter = ('join_date','status')