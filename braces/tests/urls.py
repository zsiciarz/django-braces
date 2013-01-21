from django.conf.urls.defaults import include, patterns, url

from .views import MissingHeadlineView, StaticHeadlineView, DynamicHeadlineView


urlpatterns = patterns('',
    url(r'^missing_headline/$', MissingHeadlineView.as_view(), name='missing_headline'),
    url(r'^static_headline/$', StaticHeadlineView.as_view(), name='static_headline'),
    url(r'^dynamic_headline/$', DynamicHeadlineView.as_view(), name='dynamic_headline'),
)
