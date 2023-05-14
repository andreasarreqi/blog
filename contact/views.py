from django.shortcuts import render
from django.views import generic, View
from .forms import ContactForm
from .models import Contact


class ContactUs(View):
    """
    The ContactUs view which allows the user to send a message to the admin
    """

    model = Contact
    template_name = 'contact.html'
    success_url = '/'

    def get(self, request):
        """
        Gets information through the contact form
        """
        context = {'form': ContactForm()}
        return render(request, 'contact.html', context)
