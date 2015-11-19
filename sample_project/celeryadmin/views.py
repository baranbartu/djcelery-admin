__author__ = 'baranbartu'

from django.views.generic.base import TemplateView


class ContextBasedTemplateView(TemplateView):
    context = None

    def get_context_data(self, **kwargs):
        context = super(ContextBasedTemplateView, self).get_context_data(
            **kwargs)
        context['dashboard'] = get_dashboard_context()
        return context


def get_dashboard_context():
    from contextmanager import ContextManager
    return ContextManager().dashboard
