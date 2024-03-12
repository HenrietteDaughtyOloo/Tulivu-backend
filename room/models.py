from django.db import models

# Create your models here.
Room_choices =(
    ('FS', 'Family Suite'),
    ('PS', 'Presidential Suite'),
    ('SS', 'Singles Suite'),
    ('DS', 'Double Suite'),
    ('HS', 'Honeymoon Suite'),
    ('XS', 'Extra Suite'),
)
class Room(models.Model):
    room_type = models.CharField(choices=Room_choices, max_length=2)
    room_title = models.CharField(max_length=100)
    room_price = models.FloatField()
    room_description = models.TextField()
    room_occupants_size = models.IntegerField()
    room_number = models.IntegerField()
    room_availability = models.BooleanField()
    
    def __str__(self):
        return self.room_title 