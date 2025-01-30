from django.urls import path
from . import views

### URL patterns for the reviews app

urlpatterns = [
    path('', views.index, name = 'index'),
]
