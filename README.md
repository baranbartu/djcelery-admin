# djcelery-admin

Celery task monitoring and management on custom admin page. You don't need any third party application, async process like celery-flower or any extra connection to your broker. 

# Notes

* Module will be in sample_project until end of the project. 
* celeryadmin can only work for rabbitmq, redis and mongodb brokers.
  
# Installation 

pip install git+git://github.com/baranbartu/djcelery-admin.git --upgrade

# Usage

**settings.py**

    CELERY_APPLICATION_PATH = 'sample_project.celery.app'

**INSTALLED_APPS**

    INSTALLED_APPS = (
      'celeryadmin',
    )
    
**urls.py**

    url(r'^admin/celery-monitoring/', include('celeryadmin.urls')),
    url(r'^admin/', include(admin.site.urls)), 

#ENJOY!

      /admin/celery-monitoring/dashboard/
      
      /admin/celery-monitoring/tasks/

# Screenshot

    ![ScreenShot](https://raw.github.com/baranbartu/djcelery-admin/master/screenshot1.png)
    ![ScreenShot](https://raw.github.com/baranbartu/djcelery-admin/master/screenshot2.png)
