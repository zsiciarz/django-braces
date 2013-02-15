from django.conf.urls.defaults import include, patterns, url

from .views import IndexView, MissingHeadlineView, StaticHeadlineView, \
    DynamicHeadlineView, LoginRequiredView, MissingPermissionView, \
    BadPermissionView, AddUserPermissionView, AddUserPermission403View, \
    MissingMultiplePermissionsView, BadMultiplePermissionsView, \
    AllMultiplePermissionsView, AllMultiplePermissions403View, \
    AnyMultiplePermissionsView, AnyMultiplePermissions403View, \
    SuperuserRequiredView, SuperuserRequired403View


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

    url(r'^missing_multiple_permissions/$', MissingMultiplePermissionsView.as_view(), name='missing_multiple_permissions'),
    url(r'^bad_multiple_permissions/$', BadMultiplePermissionsView.as_view(), name='bad_multiple_permissions'),
    url(r'^all_multiple_permissions/$', AllMultiplePermissionsView.as_view(), name='all_multiple_permissions'),
    url(r'^all_multiple_permissions_403/$', AllMultiplePermissions403View.as_view(), name='all_multiple_permissions_403'),
    url(r'^any_multiple_permissions/$', AnyMultiplePermissionsView.as_view(), name='any_multiple_permissions'),
    url(r'^any_multiple_permissions_403/$', AnyMultiplePermissions403View.as_view(), name='any_multiple_permissions_403'),

    url(r'^superuser_required/$', SuperuserRequiredView.as_view(), name='superuser_required'),
    url(r'^superuser_required_403/$', SuperuserRequired403View.as_view(), name='superuser_required_403'),
)
