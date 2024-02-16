from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'imgPath', 'duration', 'genre', 'language', 'mpaaRating', 'userRating')