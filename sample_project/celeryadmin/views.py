__author__ = 'baranbartu'

from django.views.generic.base import TemplateView


class ContextBasedTemplateView(TemplateView):
    context = None

    def get_context_data(self, **kwargs):
        context = super(ContextBasedTemplateView, self).get_context_data(
            **kwargs)
        context.update(self.context or {})
        context.update({'extra_content': get_dashboard_context()})
        return context


def get_dashboard_context():
    from context import Context
    return Context().dashboard
