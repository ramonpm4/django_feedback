from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(FormView):
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = 'thank-you'
    
    def form_valid(self, form) -> HttpResponse:
        form.save()
        return super().form_valid(form)
    

    # def post(self, request) -> HttpResponseRedirect | HttpResponse:
    #     form = ReviewForm(request.POST)
        
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('thank-you')
        
    #     return render(request, 'reviews/review.html', {
    #         'form': form
    #     })


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context


class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'
    
    # def get_queryset(self) -> QuerySet[Any]:
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data
    
    
class DetailReviewView(DetailView):
    template_name = 'reviews/detail_review.html'
    model = Review