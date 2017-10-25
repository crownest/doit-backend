# Django
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.contrib.auth.admin import UserAdmin as _UserAdmin

# Local
from users.models import User, ActivationKey, ResetPasswordKey


@admin.register(User)
class UserAdmin(_UserAdmin):
    fieldsets = (
        (_('Base'), {
            'fields': ('email', 'password')
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', ('image', 'image_prev'))
        }),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_verified',
                'is_superuser', 'groups', 'user_permissions'
            )
        }),
        (_('Important dates'), {
            'fields': ('last_login',)
        }),
    )
    readonly_fields = ('last_login', 'image_prev')

    add_fieldsets = (
       (None, {
           'classes': ('wide',),
           'fields': (
               'email', 'first_name', 'last_name',
               'password1', 'password2'
           )
       }),
    )

    list_display = (
        'first_name', 'last_name', 'email',
        'is_active', 'is_verified', 'is_superuser', 'image_prev'
    )
    list_filter = ('is_active', 'is_verified', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('first_name', 'last_name')


@admin.register(ActivationKey)
class ActivationKeyAdmin(admin.ModelAdmin):
    fields = ('key', 'user', 'is_used')
    readonly_fields = ('key', 'user', 'is_used')

    list_display = ('user', 'key', 'is_used')
    list_filter = ('is_used',)
    search_fields = ('user__email', 'user__first_name', 'user__last_name')


@admin.register(ResetPasswordKey)
class ResetPasswordKeyAdmin(admin.ModelAdmin):
    fields = ('key', 'user', 'is_used')
    readonly_fields = ('key', 'user', 'is_used')

    list_display = ('user', 'key', 'is_used')
    list_filter = ('is_used',)
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
