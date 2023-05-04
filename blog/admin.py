from django.contrib import admin
from .models import Musician, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Musician)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('artist', 'genre', 'slug', 'status', 'created_on')
    search_fields = ['artist', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('artist', )}
    summernote_fields = ('content', )
