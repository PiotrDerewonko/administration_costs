from django.contrib import auth
from django.db import models

class MeterLocation(models.Model):
    name = models.CharField(help_text='Nazwa kontrahenta', max_length=250)

    def __str__(self):
        return self.name

class ElectricityMeter(models.Model):
    name = models.CharField(help_text='Nazwa licznika', max_length=250)
    meter_location = models.ForeignKey(MeterLocation, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class MeterConections(models.Model):
    master_meter = models.ForeignKey(ElectricityMeter, on_delete=models.PROTECT, help_text="Licznik nadrzędy", related_name='nadlicznik')
    sub_meter = models.ForeignKey(ElectricityMeter, on_delete=models.PROTECT, help_text='Licznik podrzędny', related_name='podlicznik')
    class Meta:
        constraints = [models.UniqueConstraint(fields = ["sub_meter"], name = "unique_sub_meter",
                                               violation_error_message = 'Podany licznik był już użyty jako podlicznik. Sprawdź schemat')]


class ShareInMeter(models.Model):
    meter = models.ForeignKey(ElectricityMeter, on_delete=models.PROTECT, help_text='Nazwa licznika')
    cob_share = models.BooleanField(default=False)
    cob_share_percent = models.FloatField(default=0)
    museum_share = models.BooleanField(default=False)
    museum_share_percent = models.FloatField(default=0)
    pantheon_share = models.BooleanField(default=False)
    pantheon_share_percent = models.FloatField(default=0)
    institute_share = models.BooleanField(default=False)
    institute_share_percent = models.FloatField(default=0)
    outside_share = models.BooleanField(default=False)
    outside_share_percent = models.FloatField(default=0)

class DefaulValues(models.Model):
    name = models.CharField(max_length=250)
    value = models.FloatField(default=0)

    def __str__(self):
        return self.name

class MeterReadings(models.Model):
    meter = models.ForeignKey(ElectricityMeter, on_delete=models.PROTECT, help_text='Nazwa licznika')
    year = models.IntegerField()
    month = models.IntegerField()
    meterreading = models.FloatField()
    costperkwh = models.FloatField()
    data_reading = models.DateField()

class InvoicesCostType(models.Model):
    type = models.CharField(max_length=250, help_text='Rodzaj faktury')

    def __str__(self):
        return self.type

class InvoicesCostStatus(models.Model):
    type = models.CharField(max_length=250, help_text='Status faktury')

    def __str__(self):
        return self.type

class InvoicesCost(models.Model):
    invoice_number = models.CharField(max_length=250, help_text='Numer faktury')
    invoice_date = models.DateField()
    invoice_value = models.FloatField()
    invoice_type = models.ForeignKey(InvoicesCostType, on_delete=models.PROTECT, help_text='Rodzaj faktury')
    invoice_year_refers_to = models.IntegerField()
    invoice_month_refers_to = models.IntegerField()
    invoice_status = models.ForeignKey(InvoicesCostStatus, on_delete=models.PROTECT, help_text='Status faktury1')




