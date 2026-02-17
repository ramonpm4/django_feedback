
from django import forms

class ProfileForm(forms.Form):
    user_image = forms.ImageField() # Form control for accepting files.
