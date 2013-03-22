from django.contrib import admin


class BookCategoryAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'author', 'publication_date')
    list_filter = ('author', 'category')
    search_fields = ('title',)
    list_per_page = 3


class UserBookAdmin(admin.ModelAdmin):

    def queryset(self, request):
        """
        Show only current user's objects.
        """
        qs = super(UserBookAdmin, self).queryset(request)
        return qs.filter(owner=request.user)