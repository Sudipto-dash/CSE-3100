from django.contrib import admin
from .models import Follow, User
# Register your models here.

admin.site.register(User) #Registering User
admin.site.register(Follow)