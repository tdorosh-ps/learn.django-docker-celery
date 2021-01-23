from datetime import datetime
import io
import csv

from django.core.files.base import ContentFile

from dataschema.celery import app
from app.models import DataSchema, DataColumn, DataSet
from app.utils import gen_random_name, gen_random_job, gen_random_int, gen_random_text, gen_random_date


@app.task()
def generate_dataset_task(schema_id, rows, dataset_id):
    schema = DataSchema.objects.get(pk=schema_id)
    dataset = DataSet.objects.get(pk=dataset_id)
    temp_buffer = io.StringIO()
    delimiter = ',' if schema.column_separator == 'COM' else '.' if schema.column_separator == 'DOT' else ':'
    quotechar = "'" if schema.string_character == 'QU' else '"'
    reader = csv.writer(temp_buffer, delimiter=delimiter, quotechar=quotechar)
    columns = DataColumn.objects.filter(data_schema=schema).order_by('order')
    columns_names = [column.name for column in columns]
    reader.writerow(['#'] + columns_names)
    counter = 1
    while counter <= int(rows):
        csv_row = []
        csv_row.append(counter)
        for column in columns:
            if column.type == 'FLN':
                csv_row.append(gen_random_name())
            elif column.type == 'JOB':
                csv_row.append(gen_random_job())
            elif column.type == 'INT':
                csv_row.append(gen_random_int(column.range_from, column.range_to))
            elif column.type == 'TXT':
                csv_row.append(gen_random_text(column.range_from, column.range_to))
            elif column.type == 'DAT':
                csv_row.append(gen_random_date())
        reader.writerow(csv_row)
        counter += 1

    temp_buffer.seek(0)
    csv_content = temp_buffer.getvalue()
    temp_buffer.close()
    filename = 'fake_csv_{}.csv'.format(datetime.now().strftime('%Y-%m-%d_%H%M%S'))
    dataset.file.save(filename, ContentFile(csv_content))
