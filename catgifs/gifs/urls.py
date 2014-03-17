from django.conf.urls import url, patterns


urlpatterns = patterns(
    'gifs.views',
    url(r'^$', 'index'),
    url(r'^rate/$', 'rate'),
)
