from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('add/', views.add_item, name='add_item'),
]