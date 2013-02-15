from django.views.generic import TemplateView, FormView

from braces.views import SetHeadlineMixin, LoginRequiredMixin, \
    PermissionRequiredMixin, MultiplePermissionsRequiredMixin, \
    SuperuserRequiredMixin, StaffuserRequiredMixin, UserFormKwargsMixin

from .forms import ExampleForm


class IndexView(TemplateView):
    template_name = "braces/index.html"


class MissingHeadlineView(SetHeadlineMixin, TemplateView):
    template_name = "braces/headline.html"


class StaticHeadlineView(SetHeadlineMixin, TemplateView):
    headline = "Quick brown fox"
    template_name = "braces/headline.html"


class DynamicHeadlineView(SetHeadlineMixin, TemplateView):
    template_name = "braces/headline.html"

    def get_headline(self):
        return "Quick brown fox"


class LoginRequiredView(LoginRequiredMixin, TemplateView):
    template_name = "braces/headline.html"


class MissingPermissionView(PermissionRequiredMixin, TemplateView):
    template_name = "braces/headline.html"


class BadPermissionView(PermissionRequiredMixin, TemplateView):
    template_name = "braces/headline.html"
    permission_required = "this.has.more.than.one.dot"


class AddUserPermissionView(PermissionRequiredMixin, TemplateView):
    template_name = "braces/headline.html"
    permission_required = "auth.add_user"


class AddUserPermission403View(PermissionRequiredMixin, TemplateView):
    template_name = "braces/headline.html"
    permission_required = "auth.add_user"
    raise_exception = True


class MissingMultiplePermissionsView(MultiplePermissionsRequiredMixin, TemplateView):
    template_name = "braces/headline.html"


class NotADictMultiplePermissionsView(MultiplePermissionsRequiredMixin, TemplateView):
    template_name = "braces/headline.html"
    permissions = ['this.is.not.a.dict']


class WrongKeysMultiplePermissionsView(MultiplePermissionsRequiredMixin, TemplateView):
    template_name = "braces/headline.html"
    permissions = {
        'every': ('auth.add_user', 'auth.change_user'),
    }


class NotAListMultiplePermissionsView(MultiplePermissionsRequiredMixin, TemplateView):
    template_name = "braces/headline.html"
    permissions = {
        'all': 'auth.add_user',
    }


class AllMultiplePermissionsView(MultiplePermissionsRequiredMixin, TemplateView):
    template_name = "braces/headline.html"
    permissions = {
        'all': ('auth.add_user', 'auth.change_user'),
    }


class AllMultiplePermissions403View(MultiplePermissionsRequiredMixin, TemplateView):
    template_name = "braces/headline.html"
    permissions = {
        'all': ('auth.add_user', 'auth.change_user'),
    }
    raise_exception = True


class AnyMultiplePermissionsView(MultiplePermissionsRequiredMixin, TemplateView):
    template_name = "braces/headline.html"
    permissions = {
        'any': ('auth.add_user', 'auth.change_user'),
    }


class AnyMultiplePermissions403View(MultiplePermissionsRequiredMixin, TemplateView):
    template_name = "braces/headline.html"
    permissions = {
        'any': ('auth.add_user', 'auth.change_user'),
    }
    raise_exception = True


class SuperuserRequiredView(SuperuserRequiredMixin, TemplateView):
    template_name = "braces/headline.html"


class SuperuserRequired403View(SuperuserRequiredMixin, TemplateView):
    template_name = "braces/headline.html"
    raise_exception = True


class StaffuserRequiredView(StaffuserRequiredMixin, TemplateView):
    template_name = "braces/headline.html"


class StaffuserRequired403View(StaffuserRequiredMixin, TemplateView):
    template_name = "braces/headline.html"
    raise_exception = True


class UserFormKwargsView(UserFormKwargsMixin, FormView):
    form_class = ExampleForm
    template_name = "braces/form.html"
