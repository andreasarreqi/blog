from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    """
    PostForm allows the user to post something of their creation
    """
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'message',
        )
