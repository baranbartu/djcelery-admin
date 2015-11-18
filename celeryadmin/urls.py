from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = [
    url(r'^admin/celery-monitoring/index',
        TemplateView.as_view(
            template_name='admin/celery-monitoring/index.html')),
]
