from django.contrib import admin
from .models import Allergies, AnimalInstance, Building, Medication, Shelter_Location

# Register your models here.
# These is the basic way of registering the models to the admin site, make sure you import them above
admin.site.register(Allergies)
admin.site.register(Building)
admin.site.register(Medication)
admin.site.register(Shelter_Location)

# The decorator is one way of assigning the model to the class.
# At the momment this class allows there to be a filter in the admin site by date and status which is handy when there is a lot of animals.
@admin.register(AnimalInstance)
class AnimalInstanceAdmin(admin.ModelAdmin):
    list_filter = ('arrival_date','status')