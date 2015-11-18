# djcelery-admin
Celery task monitoring and management on custom django admin page

celery -A sample_project worker -l info

c = Control(celery_app)
c.inspect().active()