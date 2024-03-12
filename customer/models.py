from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField(max_length = 255)
    customer_phonenumber = models.CharField(max_length = 13)
    customer_email = models.EmailField()
    
    def __str__(self):
        return self.customer_name