from django.contrib import admin


class BookCategoryAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


class UserBookAdmin(admin.ModelAdmin):

    def queryset(self, request):
        """
        Show only current user's objects.
        """
        qs = super(UserBookAdmin, self).queryset(request)
        return qs.filter(owner=request.user)