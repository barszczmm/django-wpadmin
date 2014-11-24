from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst


class BookCategoryAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'author', 'publication_date')
    list_filter = ('author', 'category')
    search_fields = ('title',)
    list_per_page = 3
    fieldsets = (
        ('', {
            'fields': ('title', 'category', ('author', 'publication_date')),
        }),
        (capfirst(_('description')), {
            'fields': ('description',),
            'classes': ('collapse collapse-opened',),
        }),
        (capfirst(_('owner')), {
            'fields': ('owner',),
            'classes': ('collapse',),
        }),
    )


class UserBookAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        """
        Show only current user's objects.
        """
        qs = super(UserBookAdmin, self).queryset(request)
        return qs.filter(owner=request.user)