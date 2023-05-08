from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Musician
from .forms import CommentForm


class MusicianList(generic.ListView):
    """
    Musician List view  renders blog page posts using the Musician model
    """
    model = Musician
    queryset = Musician.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    """
    Gets the need data from the post_detail html template
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Musician.objects.filter(status=1)
        musician = get_object_or_404(queryset, slug=slug)
        comments = musician.comments.filter(
                                    approved=True).order_by("-created_on")
        liked = False
        if musician.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "musician": musician,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )
