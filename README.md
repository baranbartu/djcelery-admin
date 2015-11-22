# djcelery-admin (Still development)

Celery task monitoring and management on custom admin page
* Important Note: Module will be in sample_project until end of the project. 
  

# Installation 

pip install git+git://github.com/baranbartu/djcelery-admin.git --upgrade

**Usage**

  INSTALLED_APPS = (
      .
      .
      'celeryadmin',
  )

  url(r'^admin/celery-monitoring/', include('celeryadmin.urls')),
  url(r'^admin/', include(admin.site.urls)), 

**ENJOY!**

visit /admin/celery-monitoring/dashboard/

# Screenshot

![ScreenShot](https://raw.github.com/baranbartu/djcelery-admin/master/screenshot.png)
