from import_export import resources
from .models import AnimalInstance

class AnimalInstanceResource(resources.ModelResource):
    class Meta:
        model = AnimalInstance