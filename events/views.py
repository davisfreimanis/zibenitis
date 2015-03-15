from django.shortcuts import render, get_object_or_404
from events.models import Event


# For the sidebar (brief information)
def event_brief(request):
    events = Event.objects.order_by('date').filter(date__year='2015')
    # events = Event.objects.all()  # order_by('events__event_date') //not working?
    return render(request, 'events/events.html', {'events': events})  # A list for the side bar. Title and date


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event.html', {'event': event})  # An event with description, time, location and more