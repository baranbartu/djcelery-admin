from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/celery-monitoring/', include('celeryadmin.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
