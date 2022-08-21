from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from . import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'username']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Personal Info'),
            {
                'fields': (
                    'avatar',
                    'username',
                    'first_name',
                    'last_name',
                    'birthday',
                    'phone',
                )
            },
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            },
        ),
        (_('Important dates'), {'fields': ('last_login', 'created_at')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'username', 'password1', 'password2')}),
    )

    readonly_fields = ('created_at',)


class TrainAdmin(admin.ModelAdmin):

    list_display = ['title', 'time_create', 'author']


class ArticlesAdmin(admin.ModelAdmin):

    list_display = ['title', 'time_create', 'author']


class TrainProgramAdmin(admin.ModelAdmin):

    list_display = ['name', 'author']


admin.site.register(models.Train, TrainAdmin)
admin.site.register(models.Articles, ArticlesAdmin)
admin.site.register(models.TrainProgram, TrainProgramAdmin)
admin.site.register(models.User, UserAdmin)
