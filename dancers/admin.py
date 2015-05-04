from django.contrib import admin
from dancers.models import History
from dancers.models import Person
from dancers.models import Contact_person

# Register your models here.
admin.site.register(History)
admin.site.register(Person)
admin.site.register(Contact_person)
