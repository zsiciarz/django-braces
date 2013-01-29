from django.views.generic import TemplateView

from braces.views import SetHeadlineMixin, LoginRequiredMixin, \
    PermissionRequiredMixin, MultiplePermissionsRequiredMixin


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


class BadMultiplePermissionsView(MultiplePermissionsRequiredMixin, TemplateView):
    template_name = "braces/headline.html"
    permissions = ['this.is.not.a.dict']

