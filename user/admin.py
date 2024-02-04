from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'username', 'first_name', 'role', 'is_active']
    list_display_links = ('id', 'username', 'first_name')
    list_editable = ('is_active',)
    search_fields = ('username', 'first_name')
    list_filter = ('is_active', 'role')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
