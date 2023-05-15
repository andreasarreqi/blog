from django.shortcuts import render, redirect
from django.views import generic, View
from .forms import ContactForm
from .models import Contact


class ContactUs(View):
    """
    The ContactUs view which allows the user to send a message to the admin
    """

    model = Contact
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'

    def get(self, request):
        """
        Gets the actual form to display on the page.
        """

        context = {'form': ContactForm()}
        return render(request, 'contact.html', context)

    def post(self, request):
        """
        This function actually posts the data, sends the data to the database.
        """
        if request.method == "POST":
            form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = ContactForm()
        return render(request, 'contact.html', context)
