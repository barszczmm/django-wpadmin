import os
from setuptools import setup, find_packages
from wpadmin import VERSION


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-wpadmin',
    version='.'.join(str(x) for x in VERSION),
    description='WordPress look and feel for Django administration panel.',
    long_description = '''
%s

%s
''' % (read('README.rst'), read('docs/changelog.rst')),
    author='Maciej Marczewski (barszcz)',
    author_email='maciej@marczewski.net.pl',
    url = 'https://github.com/barszczmm/django-wpadmin',
    keywords = 'wordpress django admin',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    zip_safe = False,
)