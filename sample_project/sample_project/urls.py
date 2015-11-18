from django.conf.urls import include, url
from django.contrib import admin
from celeryadmin import urls as celery_admin_urls

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^celery-monitoring/', include(celery_admin_urls)),
]
