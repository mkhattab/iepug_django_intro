from django import forms
from django.core.exceptions import ValidationError

from .models import GIF, Rating


class GIFSubmissionForm(forms.ModelForm):
    class Meta:
        model = GIF
        fields = ['url', 'description']
        widgets = {
            'description': forms.TextInput(),
        }


class GIFRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rate', 'gif']
        widgets = {
            'rate': forms.RadioSelect(),
            'gif': forms.MultipleHiddenInput(),
        }
