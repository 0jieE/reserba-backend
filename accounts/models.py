from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name or self.username


class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shops')
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    barangay = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    subdomain = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=255)
    duration_minutes = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.shop.name}"


class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='bookings')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='bookings')
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=20)
    booking_time = models.DateTimeField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.customer_name} at {self.booking_time}"
