from django.shortcuts import render
from django.http import HttpResponse

from dancers.models import Person
from dancers.models import Picture
from dancers.forms import UploadFileForm


def index(request):
    persons = Person.objects.order_by('last_name')
#    return render(request, 'dancers/index.html', {'persons': persons})

    # Handle file upload
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        datatxt = "Here comes debugging output, I am at 1, form.is_valid = %d" %form.is_valid()
        if form.is_valid():
            newpic = Picture(pic = request.FILES['pic'])
            newpic.save()
            datatxt = str("%s, %s, " %(MEDIA_ROOT,newpic.filename) )

           # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('dancers.views.index'))

    else:
        form = UploadFileForm() # A empty, unbound form
        datatxt = "Here comes debugging output, I am at 2"

    return render(
        request,
        'dancers/index.html',
        {'persons': persons, 'form': form, 'data': datatxt}
    )
