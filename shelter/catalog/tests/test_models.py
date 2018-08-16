from django.test import TestCase
from catalog.models import Building, AnimalInstance, Allergies, Medication

class ModelTesting(TestCase):
    def setUP(self):
        build = Building.objects.create(
           room = 'Main',
           cage = 1,
        )

        AnimalInstance.objects.create(
            name = 'Dexter',
            status = 'a',
            arrival_date = datetime.now().date(),
            gender = 'm',
            cage = build,
        )

        Allergies.objects.create(
            allergy = 'Wheat'
        )

        Medication.objects.create(
            name = 'Paracetamol',
            type1 = 'p'
        )
    