from django import forms
from catalog import models

class AnimalCreateForm(forms.ModelForm):
    class Meta:
        model = models.Animal
        fields = [
            'animal_species',
            'breed',
        ]


class AnimalInstanceCreateForm(forms.ModelForm):
    class Meta:
        model = models.AnimalInstance
        exclude = (
            'species',
            'cross',
            'leaving_date',
            'caretaker',
            'diet',
        )

class ColourCreateForm(forms.ModelForm):
    class Meta:
        model = models.Colour
        fields = [
            'colorfield',
        ]

class BuildingCreateForm(forms.ModelForm):
    class Meta:
        model = models.Building
        fields = [
            'room',
            'cage',
        ]

class ShelterLocationCreateForm(forms.ModelForm):
    class Meta:
        model = models.Shelter_Location
        exclude = [
            'rooms',
        ]

class CaretakersCreateForm(forms.ModelForm):
    class Meta:
        model = models.Caretakers
        fields = [
            'first_name',
            'last_name',
            'email',
            'contactnumber1',
            'contactnumber2',
        ]

class MedicationCreateForm(forms.ModelForm):
    class Meta:
        model = models.Medication
        exclude = [
            'aniinst1',

        ]

class AllergiesCreateForm(forms.ModelForm):
    class Meta:
        model = models.Allergies
        exclude = [
            'aniinst1',
        ]

