from django.shortcuts import render
from django.http import HttpResponse

from dancers.models import History
from dancers.models import Person
from dancers.models import Contact_person


active = True


def index(request):
    history = History.objects.order_by('modified')
    persons = Person.objects.filter(active=True).order_by('last_name')
    non_active_persons = Person.objects.filter(active=False).order_by('last_name')
    return render(request, 'dancers/dancers.html', {'persons': persons, 'history': history, 'about_active': active, 'non_active_persons': non_active_persons})

