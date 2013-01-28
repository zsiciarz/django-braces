from django.conf.urls.defaults import include, patterns, url

from .views import IndexView, MissingHeadlineView, StaticHeadlineView, \
    DynamicHeadlineView, LoginRequiredView, MissingPermissionView, \
    BadPermissionView, AddUserPermissionView, AddUserPermission403View


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^missing_headline/$', MissingHeadlineView.as_view(), name='missing_headline'),
    url(r'^static_headline/$', StaticHeadlineView.as_view(), name='static_headline'),
    url(r'^dynamic_headline/$', DynamicHeadlineView.as_view(), name='dynamic_headline'),

    url(r'^login_required/$', LoginRequiredView.as_view(), name='login_required'),

    url(r'^missing_permission/$', MissingPermissionView.as_view(), name='missing_permission'),
    url(r'^bad_permission/$', BadPermissionView.as_view(), name='bad_permission'),
    url(r'^add_user_permission/$', AddUserPermissionView.as_view(), name='add_user_permission'),
    url(r'^add_user_permission_403/$', AddUserPermission403View.as_view(), name='add_user_permission_403'),
)
