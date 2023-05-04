from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Musician(models.Model):
    """
    Defines the post model attribues of the database
    """
    artist = models.CharField(max_length=200, unique=True)
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

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.artist

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Defines the comment model attribues of the database
    """
    post = models.ForeignKey(Musician,
                             on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
