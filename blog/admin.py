from django.contrib import admin
from .models import Musician, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Musician)
class PostAdmin(SummernoteModelAdmin):
    """
    Class represents the post functions on the admin panel
    """
    list_display = ('artist', 'genre', 'slug', 'status', 'created_on')
    search_fields = ['artist', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('artist', )}
    summernote_fields = ('content', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Class represents the comment functions on the admin panel
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
