from django.contrib import admin
from . models import Room

# Register your models here.
class Room_admin(admin.ModelAdmin):
    list_display = ['room_type','room_title','room_price','room_description','room_occupants_size','room_number','room_availability']
admin.site.register(Room, Room_admin)

    