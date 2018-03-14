from django.contrib import admin
from .models import History
from .models import Person
from .models import Contact_person
from markdownx.admin import MarkdownxModelAdmin


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
    list_display = [Person.__str__, 'active']
    ordering = ['first_name']
    actions = [make_inactive, make_active]


# Register your models here.
admin.site.register(History, MarkdownxModelAdmin)
admin.site.register(Person, DancersAdmin)
admin.site.register(Contact_person)
