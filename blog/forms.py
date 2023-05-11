from .models import Musician, Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = (
            'artist',
            'genre',
            'content',
            'excerpt',
            'artist_image',
        )