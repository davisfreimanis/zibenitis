import locale

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from dancers.models import Person
from stats.models import Rehearsal
from django.db.models import Count

locale.setlocale(locale.LC_ALL, "lv_LV.utf8")


def index(request):
    # persons is the active dancers in latvian alphabetic order by last name.
    persons = sorted(Person.objects.filter(active=True), key=lambda a: locale.strxfrm(a.last_name))
    rehearsals = Rehearsal.objects.all()
    stats = rehearsals.values('present_persons__first_name', 'present_persons__last_name', 'present_persons__picture').order_by('-present_persons__count').annotate(Count('present_persons'))
    return render(request, 'stats/stats.html', {'persons': persons, 'rehearsals': rehearsals, 'stats': stats})


class RehearsalCreate(CreateView):
    model = Rehearsal
    fields = ['date', 'present_persons']
    success_url = reverse_lazy('stats:index')


class RehearsalUpdate(UpdateView):
    model = Rehearsal
    fields = ['date', 'present_persons']
    success_url = reverse_lazy('stats:index')


class RehearsalDelete(DeleteView):
    model = Rehearsal
    success_url = reverse_lazy('stats:index')
