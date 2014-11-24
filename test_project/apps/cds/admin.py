from django.contrib import admin


class CdCategoryAdmin(admin.ModelAdmin):
    pass


class CdAdmin(admin.ModelAdmin):
    pass


class UserCdAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        """
        Show only current user's objects.
        """
        qs = super(UserCdAdmin, self).queryset(request)
        return qs.filter(owner=request.user)

