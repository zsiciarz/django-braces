from django.views.generic import TemplateView

from braces.views import SetHeadlineMixin


class MissingHeadlineView(SetHeadlineMixin, TemplateView):
    template_name = "braces/headline.html"


class StaticHeadlineView(SetHeadlineMixin, TemplateView):
    headline = "Quick brown fox"
    template_name = "braces/headline.html"


class DynamicHeadlineView(SetHeadlineMixin, TemplateView):
    template_name = "braces/headline.html"

    def get_headline(self):
        return "Quick brown fox"

