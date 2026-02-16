from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(View):
    
    def get(self, request) -> HttpResponse:
        form = ReviewForm()
        
        return render(request, 'reviews/review.html', {
        'form': form
        })
        
    def post(self, request) -> HttpResponseRedirect | HttpResponse:
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thank-you')
        
        return render(request, 'reviews/review.html', {
            'form': form
        })


class ThankYouView(View):
    def get(self, request) -> HttpResponse:
        return render(request, 'reviews/thank_you.html')

