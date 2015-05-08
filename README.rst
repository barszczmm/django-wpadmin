===============
Django WP Admin
===============

----------------------------------------------------------------------------------------------------------------------
`WordPress <http://wordpress.org/>`_ look and feel for `Django <http://www.djangoproject.com/>`_ administration panel.
----------------------------------------------------------------------------------------------------------------------

.. image:: https://raw.github.com/barszczmm/django-wpadmin/master/docs/images/django-wpadmin.png


Features
--------
* WordPress look and feel
* New styles for selector, calendar and timepicker widgets
* More responsive (admin panel should look fine and be usable on displays with minimum 360px width)
* Editable top menu
* Optional fully configurable left menu
* Left menu can be pinned (fixed CSS position) or unpinned and collapsed or expanded
* Awesome `Font Awesome <http://fontawesome.io/>`_ icons supported in both menus
* Multiple AdminSite's support with possibility to have different menus, colors and titles for each one
* 9 additional color themes included
* Collapsible fieldsets can be opened by default
* Python3 compatible


Django compatibility
--------------------
On GitHub there is specific branch of Django WP Admin for each major Django version and master branch is always for current stable Django.
Releases on PyPI have numbering matching proper Django versions, so for instance for Django 1.7.x you should install Django WP Admin 1.7.y
(pip install "django-wpadmin>=1.7,<1.8").
Branches of Django WP Admin for Django older than current stable usually will not have new features added, only bugs will be fixed.
Only version for current stable Django will have new features, but any pull requests for older branches are welcome.


TODO
----
* Make sure everything works fine with GeoDjango
* Do not rely on Django admin styles, move everything to Django WP Admin styles.
* Better documentation
* `django-filebrowser <https://github.com/sehmaschine/django-filebrowser>`_ or `django-filer <https://github.com/stefanfoulis/django-filer>`_ support
* `django-mptt <https://github.com/django-mptt/django-mptt>`_ support
* Optional templates for `django-rosetta <https://github.com/mbi/django-rosetta>`_


Demo
----
Try ``test_project`` `here <http://django-wpadmin.dev.barszcz.info>`_ or download `django-wpadmin <https://github.com/barszczmm/django-wpadmin>`_ from GitHub and run it on your own machine. ``test_project`` contains SQLite database file with prepopulated sample data.


Installation
------------

* Install django-wpadmin from `PyPI <https://pypi.python.org/pypi/django-wpadmin>`_::

    pip install django-wpadmin


* Or from GitHub::

    pip install git+https://github.com/barszczmm/django-wpadmin.git#egg=django-wpadmin



Basic configuration
-------------------
* Add ``wpadmin`` to your ``INSTALLED_APPS`` before ``django.contrib.admin``::

    INSTALLED_APPS = (
        # Django WP Admin must be before django.contrib.admin
        'wpadmin',
    )


* Add `django.core.context_processors.request <https://docs.djangoproject.com/en/dev/ref/templates/api/#django-core-context-processors-request>`_ to `TEMPLATE_CONTEXT_PROCESSORS <https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATE_CONTEXT_PROCESSORS>`_ setting.


Documentation
-------------

Basic configuration above will only change look of Django's admin page, but there's much more you can do with Django WP Admin.
Check out `documentation on Read the Docs <http://django-wp-admin.readthedocs.org>`_ for details (there is also **changelog** there).


Translations
------------

`Many translations are already available <http://django-wp-admin.readthedocs.org/en/master/translations.html>`_ thanks to good people that helped. If you want to help to translate this software, please join me on Transifex: `transifex.com/projects/p/django-wp-admin/ <https://www.transifex.com/projects/p/django-wp-admin/>`_


Troubleshooting
---------------

Please create an `issue on GitHub <https://github.com/barszczmm/django-wpadmin/issues>`_ if you have any problems or requests.


Credits
-------

Python code is based on `django-admin-tools <https://bitbucket.org/izi/django-admin-tools/wiki/Home>`_ app.

WordPress look and feel is of course inspired by `WordPress <http://wordpress.org/>`_.

Included icons comes from `Font Awesome <http://fontawesome.io/>`_.

