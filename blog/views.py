from django.shortcuts import render, get_object_or_404
from blog.models import Post
from events.models import Event


def blog(request):
    events = Event.objects.order_by('date')
    posts = Post.objects.order_by('-created')
    return render(request, 'blog/blog.html', {'posts': posts, 'events': events})  #


def post(request, post_id):
    events = Event.objects.order_by('date')
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post.html', {'post': post, 'events': events})
