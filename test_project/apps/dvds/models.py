from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

from authors.models import Author


@python_2_unicode_compatible
class DvdCategory(models.Model):

    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category of DVDs')
        verbose_name_plural = _('Categories of DVDs')


@python_2_unicode_compatible
class Dvd(models.Model):

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    category = models.ForeignKey(DvdCategory, verbose_name=_('category'))
    author = models.ForeignKey(Author, verbose_name=_('author'))
    owner = models.ForeignKey(User, verbose_name=_('owner'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('DVD')
        verbose_name_plural = _('DVDs')
