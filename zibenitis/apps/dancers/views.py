import locale

from django.shortcuts import render
from django.http import HttpResponse

from .models import History
from .models import Person
from .models import Contact_person

active = True
locale.setlocale(locale.LC_ALL, "lv_LV.utf8")


def index(request):
    history = History.objects.order_by('modified')
    # persons is the active dancers in latvian alphabetic order by last name.
    persons = sorted(Person.objects.filter(active=True), key=lambda a: locale.strxfrm(a.last_name))
    non_active_persons = sorted(Person.objects.filter(active=False), key=lambda a: locale.strxfrm(a.last_name))
    return render(request, 'dancers/dancers.html', {'persons': persons, 'history': history, 'about_active': active, 'non_active_persons': non_active_persons})

