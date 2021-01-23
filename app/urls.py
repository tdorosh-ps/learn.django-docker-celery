from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from app.views import DataSchemaListView, DataSchemaCreateView, DataSchemaUpdateView, DataSchemaDeleteView, \
    DataSetListView, generate_dataset


urlpatterns = [
    path('', DataSchemaListView.as_view(), name='schema-list'),
    path('schemas/create/', DataSchemaCreateView.as_view(), name='schema-create'),
    path('schemas/update/<int:schema_id>/', DataSchemaUpdateView.as_view(), name='schema-update'),
    path('schemas/delete/<int:schema_id>/', DataSchemaDeleteView.as_view(), name='schema-delete'),
    path('schemas/<int:schema_id>/datasets/', DataSetListView.as_view(), name='schema-dataset-list'),
    path('dataset/generate/', generate_dataset, name='dataset-generate')
]
