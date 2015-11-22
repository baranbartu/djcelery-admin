from django.conf.urls import url
from .views import ContextBasedTemplateView

urlpatterns = [
    url(r'^dashboard/$',
        ContextBasedTemplateView.as_view(
            template_name='admin/celery-monitoring/dashboard.html'),
        name='dashboard'),
]
