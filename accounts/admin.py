from django.contrib import admin
from .models import User, Shop, Service, Booking

admin.site.register(User)
admin.site.register(Shop)
admin.site.register(Service)
admin.site.register(Booking)
