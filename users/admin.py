from django.contrib import admin
from users.models import User
from copy import deepcopy
from django.shortcuts import get_object_or_404
from django.contrib.auth.admin import UserAdmin as _UserAdmin
from django.utils.translation import ugettext as _


@admin.register(User)
class UserAdmin(_UserAdmin):
    actions = ['delete_selected']

    add_fieldsets = (
        (None, {
                    'classes': ('wide',),
                    'fields': ('email', 'first_name', 'last_name',
                               'password1', 'password2')
               }
        ),
    )

    fieldsets = (
        (_('Base'), {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    list_display = ('first_name', 'last_name', 'email', 'is_active',
                    'is_superuser')
    list_filter = ['is_active']
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login',)
    ordering = ('first_name', 'last_name')
