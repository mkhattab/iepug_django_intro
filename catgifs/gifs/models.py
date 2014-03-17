import os

from django.db import models

class GIF(models.Model):
    url = models.URLField(unique=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return os.path.basename(self.url)
