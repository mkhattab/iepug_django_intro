from django.shortcuts import render
from django.http import HttpResponse

from .models import GIF


def index(request):
    qs = GIF.objects.order_by('?')
    gif = qs.first()

    return render(request,
                  'gifs/index.html',
                  {'cat': gif})
