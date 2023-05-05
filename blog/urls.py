from . import views
from django.urls import path


urlpatterns = [
    path("", views.MusicianList.as_view(), name="home"),
]
