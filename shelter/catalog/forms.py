from django import forms, forms
from django.core.exceptions import NON_FIELD_ERRORS
from catalog.models import AnimalInstance, Building, Shelter_Location,Medication, Allergies
from datetime import datetime



class AnimalInstanceCreateForm(forms.ModelForm):
    class Meta:
        model = AnimalInstance
        exclude = (
            'cross',
            'leaving_date',
            'adopter_first_name',
            'adopter_last_name',
            'adopter_email',
            'adopter_contactnumber1',
            'adopter_contactnumber2',
            'food_type',
            'portion_size',
            'daily_portions',
            'allergies',
            'medication',
            'medication_date_start',
            'medication_date_finish',
            'medication_weekly_dose',
            'medication_daily_dose',
        )

class AnimalInstanceAdoptForm(forms.ModelForm):
    class Meta:
        model = AnimalInstance
        fields = [
            'leaving_date',
            'status',
            'adopter_first_name',
            'adopter_last_name',
            'adopter_email',
            'adopter_contactnumber1',
            'adopter_contactnumber2',
        ]
    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['status'] != 'd':
            raise forms.ValidationError(
                'Please change the status to adopted.'
            )
        return cleaned_data

class AdopterDetailsForm(forms.ModelForm):
    class Meta:
        model = AnimalInstance
        fields = [
            'adopter_first_name',
            'adopter_last_name',
            'adopter_email',
            'adopter_contactnumber1',
            'adopter_contactnumber2',
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

class MedicationCreateForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = [
            'name',
            'type1',

        ]

class AllergiesCreateForm(forms.ModelForm):
    class Meta:
        model = Allergies
        fields = [
            'allergy',
        ]
        success_url = ''

