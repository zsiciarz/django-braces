from django.conf.urls.defaults import include, patterns, url

from .views import IndexView, MissingHeadlineView, StaticHeadlineView, \
    DynamicHeadlineView, LoginRequiredView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^missing_headline/$', MissingHeadlineView.as_view(), name='missing_headline'),
    url(r'^static_headline/$', StaticHeadlineView.as_view(), name='static_headline'),
    url(r'^dynamic_headline/$', DynamicHeadlineView.as_view(), name='dynamic_headline'),

    url(r'^login_required/$', LoginRequiredView.as_view(), name='login_required'),
)
