from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .models import Post, Comment
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'post/post_list.html', context)

def comment_create(request, post_pk):

    if request.method == 'POST':

        post = get_object_or_404(Post, pk=post_pk)

        content_form = CommentForm(request.POST)

        if content_form.is_vaild():

            Comment.objects.create(
                post=post,
                author = request.user,
                content = content
            )

            return redirect('post:post_list')