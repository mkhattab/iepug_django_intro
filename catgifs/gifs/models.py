import os

from django.db import models

class GIF(models.Model):
    url = models.URLField(unique=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return os.path.basename(self.url)


class Rating(models.Model):
    gif = models.ManyToManyField(GIF, related_name='ratings')
    rate = models.PositiveSmallIntegerField(choices=zip(range(1,6),
                                                        range(1,6)))
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{}'.format(self.rate)
