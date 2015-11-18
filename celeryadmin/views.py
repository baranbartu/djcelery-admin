__author__ = 'baranbartu'

from django.shortcuts import render_to_response
from django.template.context import RequestContext


def celery_monitoring(request):
    return render_to_response('celery-monitoring.html', {},
                              RequestContext(request))
