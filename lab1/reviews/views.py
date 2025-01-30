from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.

def index(request):
    params = {}
    return render(request, 'index.html', params)

def list_review(request):
    reviews = Review.objects.all()
    params = {'reviews': reviews}
    return render(request, 'list_review.html', params)

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_review')
    else:
        form = ReviewForm()
    params = {'form': form}
    return render(request, 'add_review.html', params)