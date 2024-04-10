from django.contrib import admin
from .models.countrymodel import *
# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Zone)