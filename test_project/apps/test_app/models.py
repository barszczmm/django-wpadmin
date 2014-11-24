import os

from django.db import models
from django.conf import settings


class TestModel(models.Model):
    """
    This is test model with all possible Django fields.
    """

    big_integer = models.BigIntegerField()
    binary = models.BinaryField()
    boolean = models.BooleanField(default=False)
    char = models.CharField(max_length=255)
    comma_separated_integer = models.CommaSeparatedIntegerField(max_length=255)
    date = models.DateField()
    date_time = models.DateTimeField()
    decimal = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()
    #file = models.FileField(upload_to='uploaded')
    file_path = models.FilePathField(
        path=os.path.join(settings.BASE_DIR, '../docs'), recursive=True)
    float = models.FloatField()
    #image = models.ImageField(upload_to='uploaded')
    integer = models.IntegerField()
    ip_address = models.IPAddressField()
    generic_ip_address = models.GenericIPAddressField()
    null_boolean = models.NullBooleanField()
    positive_integer = models.PositiveIntegerField()
    positive_small_integer = models.PositiveSmallIntegerField()
    slug = models.SlugField()
    small_integer = models.SmallIntegerField()
    text = models.TextField()
    time = models.TimeField()
    url = models.URLField()
    foreign_key = models.ForeignKey('books.Book')
    many_to_many = models.ManyToManyField('authors.Author')
    one_to_one = models.OneToOneField('auth.User')
    #html = models.TextField()

