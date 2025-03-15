from django.contrib import admin
from.models import User, OneTimePassword
class Useradmin(admin.ModelAdmin):

    list_display = ('id', 'email', 'first_name', 'last_name', 'image')
    search_fields = ['email', 'first_name', 'last_name']
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    list_per_page = 10
    
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 
                       'last_name', 
                       'image', 
                        'gender',
                       )
        }),
        
        ('Permissions', {
            'fields': ('is_staff', 
                       'is_superuser', 
                       'is_active', 
                       )
        }),
        
    )
admin.site.register(User, Useradmin)


class OneTimePasswordAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp_code', 'max_otp_try', 'otp_max_out', 'otp_created_at', 'otp_expires_at')

admin.site.register(OneTimePassword, OneTimePasswordAdmin)
    