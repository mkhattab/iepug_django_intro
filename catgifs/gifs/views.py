from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .models import GIF
from .forms import GIFSubmissionForm


def index(request):
    qs = GIF.objects.order_by('?')
    gif = qs.first()

    if request.method == 'GET':
        form = GIFSubmissionForm()
    else:
        form = GIFSubmissionForm(request.POST)

        if form.is_valid():
            new_gif = form.save()
            messages.add_message(request, messages.INFO,
                                     "Thank you for submitting!!")

    return render(request,
                  'gifs/index.html',
                  {'cat': gif,
                   'form': form})
