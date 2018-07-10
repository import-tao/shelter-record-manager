from django import forms
from catalog import models

class AnimalCreateForm(forms.ModelForm):
    class Meta:
        model = models.Animal
        fields = [
            'animal_species',
            'color',
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
            'homehistory',
            'diet',
            'medication',
            'allergies',
        )
