from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Author(models.Model):

    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    biography = models.TextField(_('biography'), blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

