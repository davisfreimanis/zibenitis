from django.shortcuts import render
from django.http import HttpResponse

from dancers.models import Person

## Very basic, test view
#def index(request):
#    return HttpResponse("Hello, you are at list of dance group participants")

def index(request):
    persons = Person.objects.order_by('last_name')
    return render(request, 'dancers/index.html', {'persons': persons})
