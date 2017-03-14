from django.contrib import admin
from dancers.models import History
from dancers.models import Person
from dancers.models import Contact_person


def make_inactive(modeladmin, request, queryset):
    """"
    modeladmin - The current ModelAdmin
    request - An HttpRequest representing the current request,
    queryset - A QuerySet containing the set of objects selected by the user.
    """
    queryset.update(active=False)


def make_active(modeladmin, request, queryset):
    """"
    modeladmin - The current ModelAdmin
    request - An HttpRequest representing the current request,
    queryset - A QuerySet containing the set of objects selected by the user.
    """
    queryset.update(active=True)

make_inactive.short_description = "Make users inactive"
make_active.short_description = "Make users active"


class DancersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'active']
    ordering = ['first_name']
    actions = [make_inactive, make_active]


# Register your models here.
admin.site.register(History)
admin.site.register(Person, DancersAdmin)
admin.site.register(Contact_person)
