===============
Django WP Admin
===============

----------------------------------------------------------------------------------------------------------------------
`WordPress <http://wordpress.org/>`_ look and feel for `Django <http://www.djangoproject.com/>`_ administration panel.
----------------------------------------------------------------------------------------------------------------------

Features
--------
* Optional fixed (in CSS positioning terms) top menu with branding, user options (change password, logout, gravatar) and any other menu items
* Optional fully configurable left menu with nice WordPress style
* Left menu can be pinned (fixed CSS position) or unpinned and collapsed or expanded
* Awesome `Font Awesome <http://fortawesome.github.com/Font-Awesome/>`_ icons supported in both menus
* Multiple AdminSite's support with possibility to have different menus, colors and title for each
* Supports Django 1.3.x, 1.4.x, 1.5.x


TODO
----
* WordPress look and feel for tables, inputs, buttons
* TinyMCE integration with WordPress theme
* `django-filebrowser <https://github.com/sehmaschine/django-filebrowser>`_ integration
* Bookmarks support


Demo
----
You can test ``sample_project`` by downloading ``django-wpadmin`` and running it on your machine or you can check it `here <http://django-wpadmin.dev.barszcz.info>`_.


Installation
------------
* Install django-wpadmin from Github: ``pip install -e git+https://github.com/barszczmm/django-wpadmin.git#egg=django-wpadmin``
* Add to your ``INSTALLED_APPS`` before ``django.contrib.admin``::

    INSTALLED_APPS = (
        # Django WP Admin must be before django.contrib.admin
        'wpadmin',
        'wpadmin.menu',
        'wpadmin.dashboard',
    )


* Copy one of files from ``django-wpadmin/wpadmin/menu/templates/admin/`` (there's one file for each supported Django version) into your ``templates/admin/`` folder and rename copied file to ``base.html`` (you can also create symbolic link).
* Add ```django.core.context_processors.request <https://docs.djangoproject.com/en/dev/ref/templates/api/#django-core-context-processors-request>`_`` to `TEMPLATE_CONTEXT_PROCESSORS <https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATE_CONTEXT_PROCESSORS>`_ setting.

Basic configuration
-------------------

Add to ``settings.py``::

    WPADMIN = {
        'admin': {
            'menu': {
                'top': 'wpadmin.menu.menus.TopMenu',
                'left': 'wpadmin.menu.menus.LeftMenu',
            }
        },
    }


Advanced configuration
----------------------
Please take a look at code in ``sample_project``.


Credits
-------
Python code is heavily based on `django-admin-tools <https://bitbucket.org/izi/django-admin-tools/wiki/Home>`_ app.
WordPress look and feel is of course inspired by `WordPress <http://wordpress.org/>`_.


