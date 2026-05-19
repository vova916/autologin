from django.contrib import admin

from .models import Room, Booking, User, Category


admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(User)
admin.site.register(Category)

