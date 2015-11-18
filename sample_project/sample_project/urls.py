from django.conf.urls import include, url
from django.contrib import admin
from celeryadmin import urls as celery_admin_urls

urlpatterns = [
    url(r'^admin/celery-monitoring/', include(celery_admin_urls)),
    url(r'^admin/', include(admin.site.urls)),
]
