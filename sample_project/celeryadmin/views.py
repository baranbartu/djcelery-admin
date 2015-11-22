from django.views.generic.base import TemplateView
from client import CeleryClient

celery_client = CeleryClient()


class ContextBasedTemplateView(TemplateView):
    context = None

    def get(self, request, *args, **kwargs):
        if request.GET.get('operation'):
            operation = request.GET.get('operation')
            parameter = request.GET.get('parameter')
            celery_client.run(operation, parameter)

        return super(ContextBasedTemplateView, self).get(request, *args,
                                                         **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ContextBasedTemplateView, self).get_context_data(
            **kwargs)
        context['dashboard'] = get_dashboard_context()
        return context


def get_dashboard_context():
    from contextmanager import ContextManager
    return ContextManager().dashboard
