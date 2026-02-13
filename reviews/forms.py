
from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='Your Name', max_length=20, error_messages= {
#         'required': 'This field is required motherfucker!',
#         'max_length': 'Your name is too long.'})
#     review_text = forms.CharField(label='Your Feedback', widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label='Your Rating', min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review 
        fields = '__all__' #            Puedo en una lista decir cuales incluir.
        # exclude = ['col_name']        O puedo decirle que columnas quiero que excluya en el form.
        labels = {
            'user_name': 'Your Name',
            'review_text': 'Your Review',
            'rating': 'Your Rating',
        }