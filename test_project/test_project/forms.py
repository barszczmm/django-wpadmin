from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm
from django.utils.translation import ugettext_lazy as _


class SuperAdminAuthenticationForm(AdminAuthenticationForm):
    """
    A custom authentication form used in the super admin admin app.
    """

    error_messages = {
        'invalid_login': _("Please enter the correct %(username)s and password "
                           "for an admin account. Note that both fields may be "
                           "case-sensitive."),
    }

    def confirm_login_allowed(self, user):
        if not user.is_active or not user.is_superuser:
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': self.username_field.verbose_name}
            )


class UserAuthenticationForm(AdminAuthenticationForm):
    """
    A custom authentication form used in the user admin app.
    """

    error_messages = {
        'invalid_login': _("Please enter the correct %(username)s and password "
                           "for an user account. Note that both fields may be "
                           "case-sensitive."),
    }

    def confirm_login_allowed(self, user):
        if not user.is_active or not user.groups.filter(name='users').count():
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': self.username_field.verbose_name}
            )

