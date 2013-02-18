from django.conf.urls.defaults import include, patterns, url

from .views import IndexView, MissingHeadlineView, StaticHeadlineView, \
    DynamicHeadlineView, LoginRequiredView, MissingPermissionView, \
    BadPermissionView, AddUserPermissionView, AddUserPermission403View, \
    MissingMultiplePermissionsView, NotADictMultiplePermissionsView, \
    WrongKeysMultiplePermissionsView, NotAListMultiplePermissionsView, \
    AllMultiplePermissionsView, AllMultiplePermissions403View, \
    AnyMultiplePermissionsView, AnyMultiplePermissions403View, \
    SuperuserRequiredView, SuperuserRequired403View, \
    StaffuserRequiredView, StaffuserRequired403View, UserFormKwargsView, \
    CsrfExemptView


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
    url(r'^not_a_dict_multiple_permissions/$', NotADictMultiplePermissionsView.as_view(), name='not_a_dict_multiple_permissions'),
    url(r'^wrong_keys_multiple_permissions/$', WrongKeysMultiplePermissionsView.as_view(), name='wrong_keys_multiple_permissions'),
    url(r'^not_a_list_multiple_permissions/$', NotAListMultiplePermissionsView.as_view(), name='not_a_list_multiple_permissions'),
    url(r'^all_multiple_permissions/$', AllMultiplePermissionsView.as_view(), name='all_multiple_permissions'),
    url(r'^all_multiple_permissions_403/$', AllMultiplePermissions403View.as_view(), name='all_multiple_permissions_403'),
    url(r'^any_multiple_permissions/$', AnyMultiplePermissionsView.as_view(), name='any_multiple_permissions'),
    url(r'^any_multiple_permissions_403/$', AnyMultiplePermissions403View.as_view(), name='any_multiple_permissions_403'),

    url(r'^superuser_required/$', SuperuserRequiredView.as_view(), name='superuser_required'),
    url(r'^superuser_required_403/$', SuperuserRequired403View.as_view(), name='superuser_required_403'),

    url(r'^staffuser_required/$', StaffuserRequiredView.as_view(), name='staffuser_required'),
    url(r'^staffuser_required_403/$', StaffuserRequired403View.as_view(), name='staffuser_required_403'),

    url(r'^user_form_kwargs/$', UserFormKwargsView.as_view(), name='user_form_kwargs'),

    url(r'^csrf_exempt/$', CsrfExemptView.as_view(), name='csrf_exempt'),
)
