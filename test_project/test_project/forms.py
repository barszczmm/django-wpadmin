from django import forms
from django.contrib.auth import authenticate
from django.contrib.admin.forms import AdminAuthenticationForm
from django.utils.translation import ugettext_lazy


class SuperAdminAuthenticationForm(AdminAuthenticationForm):
    """
    A custom authentication form used in the super admin admin app.
    """

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        message = ugettext_lazy(
            "Please enter the correct username and password "
            "for admin account. Note that both fields may be case-sensitive.")

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None or not self.user_cache.is_superuser:
                raise forms.ValidationError(message, code='invalid_login')
            elif not self.user_cache.is_active:
                raise forms.ValidationError(
                    self.error_messages['inactive'],
                    code='inactive',
                )
        return self.cleaned_data


class UserAuthenticationForm(AdminAuthenticationForm):
    """
    A custom authentication form used in the user admin app.
    """

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        message = ugettext_lazy(
            "Please enter the correct username and password "
            "for user account. Note that both fields may be case-sensitive.")

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None \
                    or not self.user_cache.groups.filter(name='users').count():
                raise forms.ValidationError(message, code='invalid_login')
            elif not self.user_cache.is_active:
                raise forms.ValidationError(
                    self.error_messages['inactive'],
                    code='inactive',
                )

        return self.cleaned_data
