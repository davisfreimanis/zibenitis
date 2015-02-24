from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

def detail(request, blog_id):
    return HttpResponse("You're looking at blog %s." % blog_id)

