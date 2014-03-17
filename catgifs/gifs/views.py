from django.shortcuts import render
from django.http import HttpResponse

from .models import GIF


def index(request):
    qs = GIF.objects.order_by('?')
    gif = qs.first()

    response = '''
    <h1>{}</h1>
    <img src={}>
    '''.format(gif.description, gif.url)

    return HttpResponse(response)
