
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ProfileForm

# Create your views here.


class CreateProfileView(View):
    def get(self, request) -> HttpResponse:
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            'form': form
        })

    def post(self, request) -> None:
        print(request.FILES['image'])
        return HttpResponseRedirect('/profiles') # type: ignore