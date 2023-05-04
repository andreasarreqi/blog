from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Musician(models.Model):
    """
    Defines the post model attribues of the database
    """
    name = models.CharField(max_length=200, unique=True)
    genre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="blog_posts")
    artist_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User,
                                   related_name='blogpost_like',
                                   blank=True)
