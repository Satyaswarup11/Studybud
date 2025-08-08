from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message, User

admin.site.register(User)  # Register the custom User model
admin.site.register(Room)
admin.site.register(Topic)  # Register the Topic model as well
admin.site.register(Message)  # Register the Message model