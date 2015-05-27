from django.shortcuts import render
from django.http import HttpResponse

from dancers.models import History
from dancers.models import Person
from dancers.models import Contact_person


def index(request):
    history = History.objects.order_by('modified')
    persons = Person.objects.order_by('last_name')
    cont_pers = Contact_person.objects.order_by('role')
    return render(request, 'dancers/index.html', {'persons': persons, 'history': history, 'cpers': cont_pers})

