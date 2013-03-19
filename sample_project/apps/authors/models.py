from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):

    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    biography = models.TextField(_('biography'), blank=True)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

