# urls.py

from django.urls import path
from .views import destination_list, destination_create, destination_update, destination_delete

urlpatterns = [
    path('', destination_list, name='destination_list'),
    path('new/', destination_create, name='destination_create'),
    path('edit/<int:pk>/', destination_update, name='destination_update'),
    path('delete/<int:pk>/', destination_delete, name='destination_delete'),
]
