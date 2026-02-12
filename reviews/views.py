from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def review(request) -> HttpResponse:
    if request.method == 'POST':
        entered_username = request.POST['username'] # recorda que viene como dictionary con key: username porque yo le puse ese nombre.
        print(entered_username)
        return HttpResponseRedirect('thank-you')
        
    return render(request, 'reviews/review.html')


def thank_you(request) -> HttpResponse:
    return render(request, 'reviews/thank_you.html')