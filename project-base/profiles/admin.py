from django.contrib import admin
from .models import User, UserFeed

# Register your models here.
admin.site.register(User)
admin.site.register(UserFeed)

