import locale

from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponse

from dancers.models import Person
from stats.models import Rehearsal

locale.setlocale(locale.LC_ALL, "lv_LV.utf8")


def index(request):
    # persons is the active dancers in latvian alphabetic order by last name.
    persons = sorted(Person.objects.filter(active=True), key=lambda a: locale.strxfrm(a.last_name))
    rehearsals = Rehearsal.objects.all()
    return render(request, 'stats/stats.html', {'persons': persons, 'rehearsals': rehearsals})


class RehearsalCreate(CreateView):
    model = Rehearsal
    fields = ['date', 'present_persons']
