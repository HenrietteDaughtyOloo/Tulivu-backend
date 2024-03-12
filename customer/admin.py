from django.contrib import admin
from .models import Customer

# Register your models here.
class Customer_admin(admin.ModelAdmin):
    list_display = ("customer_id","customer_name","customer_phonenumber","customer_email")
admin.site.register(Customer,Customer_admin)

