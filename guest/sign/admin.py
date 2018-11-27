from django.contrib import admin
from sign.models import Event, Guest
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','limit','address','start_time']

class GuestAdmin(admin.ModelAdmin):
    list_display = ['id','event','realname','phone','email','sign']

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)