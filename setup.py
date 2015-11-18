from setuptools import setup, find_packages

try:
    README = open('README').read()
except:
    README = None

setup(
    name='djcelery-admin',
    packages=find_packages(exclude=['sample_project']),
    version='0.0.1',
    url='http://github.com/baranbartu/djcelery-admin',
    license='MIT',
    long_description=README,
    author='Baran Bartu Demirci',
    author_email='bbartu.demirci@gmail.com',
    description='Celery task monitoring and management on custom admin page',
    include_package_data=True,
    install_requires=['django', 'celery', 'django-celery']
)
