from django.shortcuts import render, get_object_or_404
from events.models import Event
from datetime import datetime, timedelta

active = True


# For the sidebar (brief information)
def event_brief(request):
    now = datetime.today() - timedelta(hours=12)  # 12 hours
    upcoming_events = Event.objects.filter(date__gte=now).order_by('date')  # posts that are upcoming
    passed_events = Event.objects.filter(date__lte=now).order_by('-date')

    return render(request, 'events/events.html', {'events': upcoming_events, 'passed_events': passed_events, 'event_active': active})  # A list for the side bar. Title and date


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event.html', {'event': event, 'event_active': active})  # An event with description, time, location and more
