from django.views.generic import TemplateView

from braces.views import SetHeadlineMixin


class StaticHeadlineView(SetHeadlineMixin, TemplateView):
    headline = 'Quick brown fox'
    template_name = 'braces/headline.html'

