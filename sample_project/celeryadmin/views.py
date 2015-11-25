from django.views.generic.base import TemplateView

from . import celery_client, context_manager


class DashboardView(TemplateView):
    context = None

    def get(self, request, *args, **kwargs):
        if request.GET.get('operation'):
            operation = request.GET.get('operation')
            parameter = request.GET.get('parameter')
            celery_client.run(operation, parameter)

        return super(DashboardView, self).get(request, *args,
                                              **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(
            **kwargs)
        context['dashboard'] = context_manager.dashboard
        return context


class TasksView(TemplateView):
    context = None

    def get_context_data(self, **kwargs):
        context = super(TasksView, self).get_context_data(
            **kwargs)
        context['tasks'] = context_manager.tasks
        return context
