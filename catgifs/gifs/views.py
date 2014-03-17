from django.shortcuts import render
from django.contrib import messages
from django.http import (HttpResponse,
                         HttpResponseNotAllowed,
                         HttpResponseServerError)

from .models import GIF, Rating
from .forms import GIFSubmissionForm, GIFRatingForm


def index(request):
    qs = GIF.objects.order_by('?')
    gif = qs.first()

    rating_form = GIFRatingForm(initial={'gif': [gif.id]})

    if request.method == 'GET':
        submission_form = GIFSubmissionForm()
    else:
        submission_form = GIFSubmissionForm(request.POST)
        if submission_form.is_valid():
            new_gif = submission_form.save()
            messages.add_message(request, messages.INFO,
                                     "Thank you for submitting!!")

    return render(request,
                  'gifs/index.html',
                  {'cat': gif,
                   'submission_form': submission_form,
                   'rating_form': rating_form})


def rate(request):
    if not request.method == 'POST':
        return HttpResponseNotAllowed('Only POST requests are allowed')

    form = GIFRatingForm(request.POST)

    if form.is_valid():
        instance = form.save()
        return HttpResponse('Thank you for rating this gif!')
    else:
        error_msg = '<br>'.join(['{}: {}.'.format(f, ', '.join(e))
                               for f, e in form.errors.items()])
        response = '<h1>Rating errors</h1><br>' + error_msg
        return HttpResponseServerError(response)
