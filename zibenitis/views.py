from django.shortcuts import render, get_object_or_404
from zibenitis.apps.dancers.models import Person, Contact_person
from zibenitis.apps.events.models import Event
from zibenitis.apps.blog.models import Post
from zibenitis.apps.blog.models import Carousel
from zibenitis.apps.dancers.models import History
from datetime import datetime, timedelta

active = True


def front_page(request):
    slides = Carousel.objects.order_by('title')[:3]
    random_dancers = Person.objects.filter(active=True).order_by('?')[:4]
    now = datetime.today() - timedelta(hours=12)  # 12 hours
    upcoming_events = Event.objects.filter(date__gte=now).order_by('date')[:3]  # posts that are upcoming
    recent_news = Post.objects.order_by('-created')[:3]
    history = History.objects.all()

    context = {
        'slides': slides,
        'dancers': random_dancers,
        'events': upcoming_events,
        'news': recent_news,
        'history': history
    }

    return render(request, 'front.html', context)


def contact_persons(request):
    administration = Contact_person.objects.order_by('order')
    return render(request, 'contact.html', {'administration': administration, 'contact_active': active})
