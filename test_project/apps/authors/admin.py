from django.contrib import admin

from books.models import Book
from cds.models import Cd
from dvds.models import Dvd
from authors.models import Author


class BookInlineAdmin(admin.TabularInline):
    model = Book
    extra = 0
    readonly_fields = ('description', )


class CdInlineAdmin(admin.StackedInline):
    model = Cd


class DvdInlineAdmin(admin.StackedInline):
    model = Dvd


class AuthorAdmin(admin.ModelAdmin):
    inlines = (BookInlineAdmin, CdInlineAdmin, DvdInlineAdmin)


admin.site.register(Author, AuthorAdmin)
