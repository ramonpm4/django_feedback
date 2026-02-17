
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ProfileForm
from .models import UserProfile


# Create your views here.


class CreateProfileView(View):
    def get(self, request) -> HttpResponse:
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            'form': form
        })

    def post(self, request) -> None:
        submitted_form = ProfileForm(request.POST, request.FILES)
        
        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES['user_image'])
            profile.save()
            return HttpResponseRedirect('/profiles') # type: ignore
        
        return render(request, "profiles/create_profile.html", {
            'form': submitted_form
        }) # type: ignore