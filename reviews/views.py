from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def review(request) -> HttpResponse:
    if request.method == 'POST':
        entered_username = request.POST['username'] # recorda que viene como dictionary con key: username porque yo le puse ese nombre.
        
        if entered_username == '':
            return render(request, 'reviews/review.html', {
                'has_error': True
            })
        
        print(entered_username)
        return HttpResponseRedirect('thank-you')
        
    return render(request, 'reviews/review.html', {
        'has_error': False
    })


def thank_you(request) -> HttpResponse:
    return render(request, 'reviews/thank_you.html')