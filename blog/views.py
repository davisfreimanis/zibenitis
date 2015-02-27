from django.shortcuts import render, get_object_or_404

from blog.models import Post


def index(request):
    posts = Post.objects.order_by('-created')
    return render(request, 'blog/blog.html', {'posts': posts})


def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post.html', {'post': post})

