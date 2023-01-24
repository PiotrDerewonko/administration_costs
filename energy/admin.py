from django.contrib import admin
from energy.models import MeterConections, MeterLocation, ElectricityMeter, ShareInMeter

admin.site.register(MeterConections)
admin.site.register(MeterLocation)
admin.site.register(ElectricityMeter)
admin.site.register(ShareInMeter)