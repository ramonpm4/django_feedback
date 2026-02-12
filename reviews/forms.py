
from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label='Your Name', max_length=20, error_messages= {
        'required': 'This field is required motherfucker!',
        'max_length': 'Your name is too long.'
    })