from django.shortcuts import render, get_object_or_404
from dancers.models import Person
from events.models import Event
from blog.models import Post
from blog.models import Carousel
from dancers.models import History
from datetime import datetime, timedelta


def front_page(request):
    slides = Carousel.objects.order_by('title')[:3]
    random_dancers = Person.objects.order_by('?')[:4]
    now = datetime.today() - timedelta(hours=12)  # 12 hours
    upcoming_events = Event.objects.filter(date__gte=now).order_by('date')[:3]  # posts that are upcoming
    recent_news = Post.objects.order_by('-created')[:3]
    history = History.objects.all()
    return render(request, 'front.html', {'slides': slides, 'dancers': random_dancers, 'events': upcoming_events, 'news': recent_news, 'history': history})


def contact_persons(request):
    administration = Person.objects.order_by('last_name')
    return render(request, 'contact.html', {'administration': administration})