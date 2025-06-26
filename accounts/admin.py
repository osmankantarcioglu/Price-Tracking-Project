from django.contrib import admin
from .models import CustomUser, CruiseAlert
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

class CruiseAlertAdmin(admin.ModelAdmin):
    list_display = ('ship_name', 'sail_date', 'purchase_price', 'purchase_type', 'user_email', 'created_at')
    search_fields = ('ship_name', 'user__email')
    list_filter = ('purchase_type', 'ship_name')

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'User Email'

admin.site.register(CruiseAlert, CruiseAlertAdmin)
