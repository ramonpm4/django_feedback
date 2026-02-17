
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

# Create your views here.


class CreateProfileView(View):
    def get(self, request) -> HttpResponse:
        return render(request, "profiles/create_profile.html")

    def post(self, request) -> None:
        print(request.FILES['image'])
        return HttpResponseRedirect('/profiles') # type: ignore