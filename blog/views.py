from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post
from events.models import Event


def blog(request):
    events = Event.objects.order_by('date')

    posts_all = Post.objects.order_by('-created')
    paginator = Paginator(posts_all, 3) # use 3 posts for testing

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/blog.html', {'posts': posts, 'events': events})  #


def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post.html', {'post': post})
