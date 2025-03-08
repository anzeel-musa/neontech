from django.contrib import admin
from.models import *

# Register your models here.
admin.site.register(Technician)
admin.site.register(Customer)
admin.site.register(Appointment)
admin.site.register(DeviceDischargeDetails)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'content', 'timestamp', 'created_at')
    search_fields = ['sender', 'recipient']
    list_filter = ('timestamp',)
    autocomplete_fields = ('sender', 'recipient')
    list_per_page = 10
admin.site.register(Message, MessageAdmin)