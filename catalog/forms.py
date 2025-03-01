from django import forms, forms
from django.core.exceptions import NON_FIELD_ERRORS
from catalog.models import AnimalInstance, Building, Shelter_Location,Medication, Allergies
from datetime import datetime
from django.utils import timezone



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

    def clean_arrival_date(self):
        arrival_date = self.cleaned_data.get('arrival_date')
        if not arrival_date:
            raise forms.ValidationError('Arrival date is required.')
            
        # Ensure the date is timezone aware
        if timezone.is_naive(arrival_date):
            arrival_date = timezone.make_aware(arrival_date)
            
        # Compare with current time in the same timezone
        if arrival_date > timezone.now():
            raise forms.ValidationError('Arrival date cannot be in the future.')
        return arrival_date

    def clean(self):
        cleaned_data = super().clean()
        required_fields = {
            'animal_species': 'Animal species is required.',
            'breed': 'Breed is required.',
            'name': 'Name is required.',
            'bio': 'Bio is required.',
            'status': 'Status is required.',
            'arrival_date': 'Arrival date is required.',
            'gender': 'Gender is required.',
            'hair_type': 'Hair type is required.',
            'hair_length': 'Hair length is required.',
        }

        for field, error in required_fields.items():
            if not cleaned_data.get(field):
                self.add_error(field, error)

        return cleaned_data

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

    def clean_status(self):
        status = self.cleaned_data.get('status')
        if status != 'd':
            raise forms.ValidationError('Please change the status to adopted.')
        return status

    def clean_leaving_date(self):
        leaving_date = self.cleaned_data.get('leaving_date')
        if not leaving_date:
            raise forms.ValidationError('Leaving date is required.')
        
        # Ensure the date is timezone aware
        if timezone.is_naive(leaving_date):
            leaving_date = timezone.make_aware(leaving_date)
            
        # Compare with current time in the same timezone
        if leaving_date > timezone.now():
            raise forms.ValidationError('Leaving date cannot be in the future.')
        return leaving_date

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')

        if status == 'd':
            required_fields = {
                'adopter_first_name': 'First name is required when adopting.',
                'adopter_last_name': 'Last name is required when adopting.',
                'adopter_email': 'Email is required when adopting.',
                'adopter_contactnumber1': 'Primary contact number is required when adopting.',
            }

            for field, error in required_fields.items():
                if not cleaned_data.get(field):
                    self.add_error(field, error)

        return cleaned_data

    def clean_adopter_contactnumber1(self):
        number = self.cleaned_data.get('adopter_contactnumber1')
        if number and not number.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')
        return number

    def clean_adopter_contactnumber2(self):
        number = self.cleaned_data.get('adopter_contactnumber2')
        if number and not number.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')
        return number if number else None

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

    def clean_cage(self):
        cage = self.cleaned_data.get('cage')
        if cage is not None and cage <= 0:
            raise forms.ValidationError('Cage number must be positive.')
        return cage

    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get('room')
        cage = cleaned_data.get('cage')

        if room and cage and Building.objects.filter(room=room, cage=cage).exists():
            raise forms.ValidationError('This cage and room combination already exists.')
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

