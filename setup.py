from setuptools import setup, find_packages

setup(
    name='djcelery-admin',
    packages=find_packages(exclude=['sample_project']),
    version='0.0.1',
    url='http://github.com/baranbartu/djcelery-admin',
    license='MIT',
    author='Baran Bartu Demirci',
    author_email='bbartu.demirci@gmail.com',
    description='Celery task monitoring and management on custom admin page',
    include_package_data=True,
    install_requires=['django', 'celery', 'django-celery']
)
