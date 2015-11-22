# djcelery-admin (Still development)

Celery task monitoring and management on custom admin page. You don't need any third party application, async process like celery-flower or any extra connection to your broker. 

# Notes

* Module will be in sample_project until end of the project. 
* celeryadmin can work only rabbitmq, redis and mongodb brokers.
  
# Installation 

pip install git+git://github.com/baranbartu/djcelery-admin.git --upgrade

# Usage

**Installed Apps**

    INSTALLED_APPS = (
      'celeryadmin',
    )
    
**urls.py**

    url(r'^admin/celery-monitoring/', include('celeryadmin.urls')),
    url(r'^admin/', include(admin.site.urls)), 

#ENJOY!

visit /admin/celery-monitoring/dashboard/

# Screenshot

![ScreenShot](https://raw.github.com/baranbartu/djcelery-admin/master/screenshot.png)
