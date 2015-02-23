from django.shortcuts import render
from django.http import HttpResponse

# Very basic, test view
def index(request):
    return HttpResponse("Hello, you are at list of dance group participants")
