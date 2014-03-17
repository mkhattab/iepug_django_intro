from django import forms

from .models import GIF


class GIFSubmissionForm(forms.ModelForm):
    class Meta:
        model = GIF
        fields = ['url', 'description']
        widgets = {
            'description': forms.TextInput(),
        }
