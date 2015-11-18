from setuptools import setup, find_packages

setup(
    name='djcelery-admin',
    version='0.0.1',
    packages=find_packages(),
    url='http://github.com/baranbartu/djcelery-admin',
    license='MIT',
    author='Baran Bartu Demirci',
    author_email='bbartu.demirci@gmail.com',
    description='Celery task monitoring and management on custom django admin page',
    install_requires=['celery', 'django-celery']
)
