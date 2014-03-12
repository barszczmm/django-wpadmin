from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

from authors.models import Author


@python_2_unicode_compatible
class CdCategory(models.Model):

    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category of CDs')
        verbose_name_plural = _('Categories of CDs')


@python_2_unicode_compatible
class Cd(models.Model):

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    category = models.ForeignKey(CdCategory, verbose_name=_('category'))
    author = models.ForeignKey(Author, verbose_name=_('author'))
    owner = models.ForeignKey(User, verbose_name=_('owner'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('CD')
        verbose_name_plural = _('CDs')

