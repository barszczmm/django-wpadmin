"""
django_wpadmin is a collection of extensions/tools for the default Django
administration panel which makes it look and behave more like WordPress
administration panel.
"""
VERSION = (1, 8, 0)

try:
    from django import VERSION as DJANGO_VERSION

    if VERSION[:2] != DJANGO_VERSION[:2]:
        import warnings
        warnings.warn(
            'Django WP Admin %(wpadmin_version)s was not tested with '
            'Django %(django_version)s and may not work properly. '
            'You may try to install Django WP Admin from %(branch)s branch.'
            % {'wpadmin_version': '.'.join(str(x) for x in VERSION),
               'django_version': '.'.join(str(x) for x in DJANGO_VERSION[:3]),
               'branch': '.'.join([str(x) for x in DJANGO_VERSION[:2]] + ['x'])},
            UserWarning)
except ImportError:
    pass
