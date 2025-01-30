from django.shortcuts import render
from .models import Review

# Create your views here.

def index(request):
    params = {}
    return render(request, 'index.html', params)