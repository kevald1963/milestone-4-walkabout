from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Unregister the provided model admin
admin.site.unregister(User)

# Register our own model admin, based on the default UserAdmin.
# This extends the User model rather than replacing it.


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    # Disable last_login and date_joined fields. These should never be editable.
    readonly_fields = [
        'last_login',
        'date_joined',
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        # Only allow superusers to modify username, is_active, etc.
        if not is_superuser:
            form.base_fields['username'].disabled = True
            form.base_fields['is_active'].disabled = True
        return form
