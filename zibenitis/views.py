from django.shortcuts import render, get_object_or_404
from dancers.models import Person


def contact_persons(request):
    administration = Person.objects.order_by('last_name')
    return render(request, 'contact.html', {'administration': administration})