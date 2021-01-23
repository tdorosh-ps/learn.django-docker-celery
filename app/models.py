from django.db import models
from django.conf import settings

# Create your models here.


class DataSchema(models.Model):
    COM = 'COM'
    DOT = 'DOT'
    COL = 'COL'
    QU = 'QU'
    DQ = 'DQ'
    COLUMN_SEPARATOR_CHOICES = [
        (COM, 'Comma'),
        (DOT, 'Dot'),
        (COL, 'Colon'),
    ]

    STRING_CHARACTER_CHOICES = [
        (QU, 'Quote'),
        (DQ, 'Double-quote'),
    ]
    name = models.CharField(max_length=50)
    column_separator = models.CharField(max_length=3, choices=COLUMN_SEPARATOR_CHOICES, default=COM)
    string_character = models.CharField(max_length=2, choices=STRING_CHARACTER_CHOICES, default=DQ)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class DataColumn(models.Model):
    FULL_NAME = 'FLN'
    JOB = 'JOB'
    INTEGER = 'INT'
    TEXT = 'TXT'
    DATE = 'DAT'
    DATA_COLUMN_TYPE_CHOICES = [
        (FULL_NAME, 'Full name'),
        (JOB, 'Job'),
        (INTEGER, 'Integer'),
        (TEXT, 'Text'),
        (DATE, 'Date'),
    ]
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=3, choices=DATA_COLUMN_TYPE_CHOICES)
    order = models.PositiveSmallIntegerField()
    range_from = models.PositiveSmallIntegerField(null=True, blank=True)
    range_to = models.PositiveSmallIntegerField(null=True, blank=True)
    data_schema = models.ForeignKey(DataSchema, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class DataSet(models.Model):
    PROGRESSING = 'PR'
    READY = 'RD'
    DATA_SET_STATUS_CHOICES = [
        (PROGRESSING, 'Progressing'),
        (READY, 'Ready')
    ]
    status = models.CharField(max_length=3, choices=DATA_SET_STATUS_CHOICES, default=PROGRESSING)
    file = models.FileField(upload_to='data_sets/', null=True, blank=True)
    data_schema = models.ForeignKey(DataSchema, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

