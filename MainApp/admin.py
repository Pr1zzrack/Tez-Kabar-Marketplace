from django.contrib import admin
from .models import *


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1

class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]

admin.site.register(Car, CarAdmin)
admin.site.register(Marka)
admin.site.register(Body)
admin.site.register(BodyColor)
admin.site.register(Year)
admin.site.register(Checkpoint)
admin.site.register(DriveUnit)
admin.site.register(StreengWhell)
