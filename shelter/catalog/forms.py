from django import forms, forms
from django.core.exceptions import NON_FIELD_ERRORS
from catalog.models import Animal, AnimalInstance, Building, Colour, Shelter_Location, Caretakers, Medication, Allergies

class AnimalCreateForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            'animal_species',
            'breed',
        ]


class AnimalInstanceCreateForm(forms.ModelForm):
    class Meta:
        model = AnimalInstance
        exclude = (
            'species',
            'cross',
            'leaving_date',
            'caretaker',
            'diet',
        )

class AnimalInstanceAdoptForm(forms.ModelForm):
    class Meta:
        model = AnimalInstance
        fields = [
            'status',
            'leaving_date',
            'cage',
        ]

class NewCartakerAdoptForm(forms.ModelForm):
    class Meta:
        model = Caretakers
        fields = '__all__'
        exclude = [
            'date_from',
            'date_to',
        ]

class ColourCreateForm(forms.ModelForm):
    class Meta:
        model = Colour
        fields = [
            'colorfield',
        ]

class BuildingCreateForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = [
            'room',
            'cage',
        ]
# Custom validation to ensure the same cage cannot be added twice
    def clean(self):
        cleaned_data = self.cleaned_data
        if Building.objects.filter(room=cleaned_data['room'],
                                   cage=cleaned_data['cage']).exists():
            raise forms.ValidationError(
                  'This cage and room combination already exist.')
        # Always return cleaned_data
        return cleaned_data

class ShelterLocationCreateForm(forms.ModelForm):
    class Meta:
        model = Shelter_Location
        exclude = [
            'rooms',
        ]

class CaretakersCreateForm(forms.ModelForm):
    class Meta:
        model = Caretakers
        fields = [
            'first_name',
            'last_name',
            'email',
            'contactnumber1',
            'contactnumber2',
        ]

class MedicationCreateForm(forms.ModelForm):
    class Meta:
        model = Medication
        exclude = [
            'aniinst1',

        ]

class AllergiesCreateForm(forms.ModelForm):
    class Meta:
        model = Allergies
        exclude = [
            'aniinst1',
        ]

