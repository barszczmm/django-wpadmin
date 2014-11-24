from django.contrib import admin


class DvdCategoryAdmin(admin.ModelAdmin):
    pass


class DvdAdmin(admin.ModelAdmin):
    pass


class UserDvdAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        """
        Show only current user's objects.
        """
        qs = super(UserDvdAdmin, self).queryset(request)
        return qs.filter(owner=request.user)

