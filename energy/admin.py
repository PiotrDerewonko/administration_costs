from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . models import MeterConections
from energy.models import MeterConections, MeterLocation, ElectricityMeter, ShareInMeter, DefaulValues, MeterReadings, \
    InvoicesCostType, InvoicesCost, InvoicesCostStatus


class ElectricityMeterAdmin(admin.ModelAdmin):
    list_display = ['name', 'meter_location']

class MeterConectionsAdmin(admin.ModelAdmin):
    model = MeterConections
    list_display = ['id', 'licznik_nadrzedny', 'podlicznik']
    def licznik_nadrzedny(self, obj):
        return obj.master_meter.name

    def podlicznik(self, obj):
        return obj.sub_meter.name

class MeterLocationAdmin(admin.ModelAdmin):
    list_display = ['name']

class SherInMeterAdmin(admin.ModelAdmin):
    list_display = ['licznik', 'cob_share', 'cob_share_percent' , 'museum_share', 'museum_share_percent'
                    , 'pantheon_share', 'pantheon_share_percent', 'institute_share', 'institute_share_percent',
                    'outside_share', 'outside_share_percent', 'suma']

    def licznik(self, obj):
        return obj.meter.name

    #todo dodac walidacje tak, aby sprawdzal czy suma wpisanaych procentow jest rowna 1 w round
    def suma(self, obj):
        return round(obj.cob_share_percent + obj.museum_share_percent + obj.pantheon_share_percent + \
               obj.institute_share_percent + obj.outside_share_percent, 1)

class MeterReadingsAdmin(admin.ModelAdmin):
    model = MeterReadings
    list_display = ['licznik', 'rok', 'miesiac', 'wartosc_licznika']

    def licznik(self, obj):
        return obj.meter.name

    def rok(self, obj):
        return obj.year

    def miesiac(self, obj):
        return obj.month

    def wartosc_licznika(self, obj):
        return obj.meterreading

class InvoiceCostAdmin(admin.ModelAdmin):
    model =  InvoicesCost
    list_display = ['invoice_number', 'invoice_date', 'invoice_value', 'invoice_type', 'invoice_year_refers_to', 'invoice_month_refers_to']


admin.site.register(MeterConections, MeterConectionsAdmin)
admin.site.register(MeterLocation, MeterLocationAdmin)
admin.site.register(ElectricityMeter, ElectricityMeterAdmin)
admin.site.register(ShareInMeter, SherInMeterAdmin)
admin.site.register(DefaulValues)
admin.site.register(MeterReadings, MeterReadingsAdmin)
admin.site.register(InvoicesCostType)
admin.site.register(InvoicesCost, InvoiceCostAdmin)
admin.site.register(InvoicesCostStatus)