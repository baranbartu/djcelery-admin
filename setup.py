from setuptools import setup, find_packages

try:
    README = open('README').read()
except:
    README = None

setup(
    name='djcelery-admin',
    version='0.0.1',
    description='Celery task monitoring and management on custom admin page',
    long_description=README,
    license='MIT',
    author='Baran Bartu Demirci',
    author_email='bbartu.demirci@gmail.com',
    packages=find_packages(exclude=['sample_project']),
    package_data={'celeryadmin': ['templates/dashboard/dashboard.html',
                                  'templates/dashboard/tasks.html']},
    include_package_data=True,
    url='http://github.com/baranbartu/djcelery-admin',
    install_requires=['django-celery']
)
