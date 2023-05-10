from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Musician, Comment
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
            'post_detail.html',
            {
                'musician': musician,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm(),
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Musician.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "musician": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
            },
        )


class PostLike(View):
    """
    PostLike view  renders blog page likes
    """
    def post(self, request, slug, *args, **kwargs):
        musician = get_object_or_404(Musician, slug=slug)
        if musician.likes.filter(id=request.user.id).exists():
            musician.likes.remove(request.user)
        else:
            musician.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
