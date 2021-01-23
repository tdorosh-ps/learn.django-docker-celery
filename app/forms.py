from django.forms import ModelForm, modelformset_factory

from app.models import DataSchema, DataColumn


class DataSchemaForm(ModelForm):
    class Meta:
        model = DataSchema
        fields = ('name', 'column_separator', 'string_character')


class DataColumnForm(ModelForm):
    class Meta:
        model = DataColumn
        fields = ('name', 'type', 'order', 'range_from', 'range_to')


DataColumnFormSet = modelformset_factory(DataColumn, DataColumnForm, extra=5, min_num=1)
