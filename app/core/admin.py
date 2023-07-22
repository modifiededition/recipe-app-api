"""
Django admin customization.
"""
from  django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from core import models

class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    search_fields = ['id']
    fieldsets = (
        (None, {'fields':('email','name')}),
        (
            _('Permissions'),
            {
                'fields':(
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        (
            _("Important dates"),
            {
                'fields':(
                    'last_login',
                )
            }
        )
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None,{
            'classes' : ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser'
            )
        }),
    )

# here we are trying to customize the base UserAdmin, we change the name as BaseUserAdmin
# So, we dont get confuse with our customized UserAdmin class name.
# here below in the method we are passing our name of customized admin class
# if we dont we will get the default display on the admin page.

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Recipe)

