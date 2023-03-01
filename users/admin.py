from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class UserUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + \
        ('adres', 'ilce', 'il', 'ülke', 'telefon')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('adres', 'ilce', 'il', 'ülke', 'telefon')}),
    )


admin.site.unregister(User)
admin.site.register(User, UserUserAdmin)
