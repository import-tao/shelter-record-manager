from import_export import resources, fields
from import_export.widgets import DateTimeWidget
from .models import AnimalInstance

class AnimalInstanceResource(resources.ModelResource):
    arrival_date = fields.Field(
        column_name='arrival_date',
        attribute='arrival_date',
        widget=DateTimeWidget(format='%m/%d/%Y %H:%M:%S')
    )
    leaving_date = fields.Field(
        column_name='leaving_date',
        attribute='leaving_date',
        widget=DateTimeWidget(format='%m/%d/%Y %H:%M:%S')
    )

    class Meta:
        model = AnimalInstance
        import_id_fields = []
        fields = ('animal_species', 'breed', 'name', 'cross', 'bio', 'status', 
                 'arrival_date', 'leaving_date', 'gender', 'hair_type', 'hair_length')
        
    def before_import_row(self, row, **kwargs):
        # Convert cross to boolean
        if 'cross' in row:
            row['cross'] = bool(int(row['cross']))
        return row