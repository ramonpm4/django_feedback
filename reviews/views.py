from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def review(request) -> HttpResponse:
    return render(request, 'reviews/review.html')