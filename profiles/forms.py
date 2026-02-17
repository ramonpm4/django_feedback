
from django import forms

class ProfileForm(forms.Form):
    user_image = forms.FileField() # Form control for accepting files.
