from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Musician, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm, PostForm


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


class AddPost(View):
    """allow user to add a post"""

    def get(self, request):
        """to get add_post.html
        using PostForm
        """
        context = {'form': PostForm()}
        return render(request, 'add_post.html', context)

    def post(self, request):
        """
        to allow user to post new articles to
        the blog for others to see and interact with.
        If the form is not valid it will display an error
        message and return to the add post form.

        If is valid form, it will save and display a success
        message to the user, as well as redirect to the
        home page
        """

        if request.method == 'POST':
            form = PostForm(request.POST, initial={
                'author': request.user.username
                })
            if form.is_valid():
                form.instance.email = request.user.email
                form.instance.name = request.user.username
                form.instance.author = self.request.user
                form.save()
                return redirect('home')
            else:
                return render(request, 'add_post.html',
                {
                    'form': form
                    }
                )
        else:
            form = PostForm()

        return render(request, 'index.html',
        {
            'form': form
        }
        )


class SharedPostsByUsers(LoginRequiredMixin, generic.ListView):
    """
    display all the posts added by currently
    logged in user, 6 posts per page
    """
    model = Musician
    author = Musician.author
    login_url = 'account_login'
    template_name = 'shared_posts.html'
    paginate_by = 6

    def get_queryset(self, *args, **kwargs):
        return Musician.objects.filter(author=self.request.user, status=1).order_by('-created_on')  # noqa: E501


class UpdatePost(UpdateView):
    """
    update a post when user logged in
    and shared a post, and they are the
    author of that post
    """
    model = Musician
    template_name = 'update_post.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        """
        if form is valid below message will display
        while return to the home page
        """
        return super().form_valid(form)


class DeletePost(DeleteView):
    """
    delete a post when user logged in
    and shared a post, and they are the
    author of that post
    """
    model = Musician
    template_name = 'delete_post.html'
    success_url = '/'
