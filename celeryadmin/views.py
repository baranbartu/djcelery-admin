from django.views.generic.base import TemplateView
from django.shortcuts import redirect

from . import celery_client, context_manager


class DashboardView(TemplateView):
    context = None

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


# todo find a better way for operations, temporary solution
class OperationsRedirectView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.GET.get('command'):
            command = request.GET.get('command')
            parameter = request.GET.get('parameter')
            celery_client.execute(command, parameter)
            return redirect('dashboard')
