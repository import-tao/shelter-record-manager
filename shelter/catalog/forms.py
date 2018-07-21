from django import forms, forms
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
    '''override the validation for this so that we can check if the new
     form contains a room/cage combination already saved to the database
    ********************************************************************
    ********************************************************************
    ********************************************************************
    ***********TO DO as it is not currently working*********************
    ********************************************************************
    ********************************************************************
    ********************************************************************
    '''
    def clean(self):
        cleaned_data = super().clean()
        room =  cleaned_data.get('room')
        cage = cleaned_data.get('cage')
        #if room and cage fields are valid...
        if cage:
            if cage in Building.objects.all():
                raise forms.ValidationError(
                'This cage already exists. Please try again'
            )
        elif room and cage:
            if room in Building.objects.all() and cage in Building.objects.all():
                raise forms.ValidationError(
                    'This room and cage combination is already in use. Please try again.'
                )

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

