from django.contrib import admin
from .models import Desktop, Printer, Ups, MultifunctionalDevice, LogoPic

# Register your models here
admin.site.register(Desktop)
admin.site.register(Printer)
admin.site.register(Ups)
admin.site.register(MultifunctionalDevice)
admin.site.register(LogoPic)
