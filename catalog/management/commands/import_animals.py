from django.core.management.base import BaseCommand
from tablib import Dataset
from catalog.resources import AnimalInstanceResource

class Command(BaseCommand):
    help = 'Import animals from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        dataset = Dataset()
        csv_file = options['csv_file']
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            imported_data = dataset.load(f.read(), format='csv')
            
        resource = AnimalInstanceResource()
        result = resource.import_data(dataset, dry_run=False)
        
        if result.has_errors():
            self.stdout.write(self.style.ERROR('Failed to import data'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Successfully imported {len(result.rows)} animals')) 