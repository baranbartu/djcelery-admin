from django.conf.urls import url
from .views import DashboardView, TasksView, OperationsRedirectView

urlpatterns = [
    url(r'^dashboard/$',
        DashboardView.as_view(
            template_name='admin/celery-monitoring/dashboard.html'),
        name='dashboard'),
    url(r'^operations/$',
        OperationsRedirectView.as_view(),
        name='operations'),
    url(r'^tasks/$',
        TasksView.as_view(
            template_name='admin/celery-monitoring/tasks.html'),
        name='tasks'),

]
