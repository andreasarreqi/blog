from . import views
from django.urls import path


urlpatterns = [
    path('contact', views.ContactUs.as_view(), name='contact'),
]
