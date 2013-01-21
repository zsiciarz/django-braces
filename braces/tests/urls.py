from django.conf.urls.defaults import include, patterns, url

from .views import StaticHeadlineView


urlpatterns = patterns('',
    url(r'^static_headline/$', StaticHeadlineView.as_view(), name='static_headline'),
)
