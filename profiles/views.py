
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView

# Create your views here.

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = '/profiles'

