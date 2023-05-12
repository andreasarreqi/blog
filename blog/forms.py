from .models import Musician, Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    CommentForm allows the user to comment on a blog post
    """
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """
    PostForm allows the user to post something of their creation
    """
    class Meta:
        model = Musician
        fields = (
            'artist',
            'genre',
            'content',
            'excerpt',
            'artist_image',
        )