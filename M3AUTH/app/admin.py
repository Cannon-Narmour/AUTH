from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Ambassador)
admin.site.register(Job)
admin.site.register(Order)