# Generated by Django 2.0.6 on 2018-09-04 13:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('allergy', models.CharField(blank=True, max_length=35, null=True)),
            ],
            options={
                'verbose_name_plural': 'Allergies',
                'ordering': ('allergy',),
            },
        ),
        migrations.CreateModel(
            name='AnimalInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('animal_species', models.CharField(blank=True, help_text='What species of animal.', max_length=30)),
                ('breed', models.CharField(blank=True, help_text='What breed of animal it is.', max_length=40)),
                ('name', models.CharField(help_text='The name of the animal.', max_length=30)),
                ('cross', models.NullBooleanField(default=False, help_text='Is the animal a cross breed? if not sure select No.')),
                ('bio', models.TextField(help_text='Enter a brief description about the animal and their personality.                                                          This may include distinctive markings,                                                         additional behaviour or care comments.', max_length=1000)),
                ('status', models.CharField(choices=[('a', 'Available'), ('q', 'Quarantine'), ('r', 'Reserved'), ('d', 'Adopted')], help_text='Select the best fit status for the animal.', max_length=1)),
                ('arrival_date', models.DateTimeField(help_text='Date animal started at the shelter.')),
                ('leaving_date', models.DateTimeField(blank=True, help_text='Date animal left the shelter.', null=True)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='f', max_length=6)),
                ('hair_type', models.CharField(blank=True, choices=[('f', 'Flat'), ('c', 'Curly'), ('w', 'Wiry'), ('f', 'Fluffy'), ('s', 'Smooth')], help_text='Please select the type of hair it has.', max_length=1)),
                ('hair_length', models.CharField(blank=True, choices=[('l', 'Long'), ('s', 'Short'), ('m', 'Medium'), ('h', 'Hairless')], default='s', help_text='Please select the length of the hair.', max_length=1)),
                ('adopter_first_name', models.CharField(blank=True, max_length=30, verbose_name='First Name')),
                ('adopter_last_name', models.CharField(blank=True, max_length=30, verbose_name='Last Name')),
                ('adopter_email', models.EmailField(blank=True, help_text='Please enter a valid email address', max_length=254, verbose_name='Email')),
                ('adopter_contactnumber1', models.CharField(blank=True, default=0, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Primary Contact Number')),
                ('adopter_contactnumber2', models.CharField(blank=True, default=0, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Secondary Contact Number')),
                ('food_type', models.CharField(blank=True, choices=[('h', 'Hard'), ('s', 'Soft')], max_length=1)),
                ('portion_size', models.FloatField(blank=True, default=1, help_text='How big is each portion of food in lbs?')),
                ('daily_portions', models.FloatField(blank=True, default=1, help_text='How many meals per day?', verbose_name='Meals per day')),
                ('medication_date_start', models.DateField(blank=True, null=True, verbose_name='Date Medication Started')),
                ('medication_date_finish', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('medication_weekly_dose', models.IntegerField(blank=True, help_text='How many days in the week need medication                                                 e.g. 3 times a day every day would mean this is 7- a dose required each day.', null=True, verbose_name='Weekly Dose')),
                ('medication_daily_dose', models.IntegerField(blank=True, help_text='How many times per day.', null=True, verbose_name='Daily Dose')),
                ('allergies', models.ManyToManyField(blank=True, help_text='Ctrl+click to select multiple/deselect', to='catalog.Allergies')),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('room', models.CharField(max_length=20)),
                ('cage', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['-room', 'cage'],
            },
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Medication')),
                ('type1', models.CharField(choices=[('p', 'Pill'), ('i', 'Injection'), ('c', 'Cream'), ('d', 'Drops')], max_length=1, verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='Shelter_Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_or_name', models.CharField(help_text='Please enter the house number or name.', max_length=20)),
                ('street', models.CharField(help_text='Street name', max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('province', models.CharField(max_length=30)),
                ('code', models.CharField(help_text='Please enter the ZIP code / postcode.', max_length=15)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('date_to', models.DateField(blank=True, null=True)),
                ('name', models.CharField(help_text='Please enter the name of the shelter building.', max_length=40, verbose_name='Building Name')),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Building')),
            ],
            options={
                'verbose_name': 'Shelter Location',
                'verbose_name_plural': 'Shelter Locations',
            },
        ),
        migrations.AddField(
            model_name='animalinstance',
            name='cage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Building'),
        ),
        migrations.AddField(
            model_name='animalinstance',
            name='medication',
            field=models.ManyToManyField(blank=True, to='catalog.Medication'),
        ),
    ]
