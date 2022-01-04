from django.contrib import admin

# import the model djangoClasses from models
from .models import djangoClasses

# register djangoClasses in admin
admin.site.register(djangoClasses)

# Register your models here.
