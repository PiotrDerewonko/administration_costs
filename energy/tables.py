import django_tables2 as tables
from . models import InvoicesCost, MeterReadings

class InvoiceTable(tables.Table):
    class Meta:
        model = InvoicesCost


class MeterReadingTable(tables.Table):
    class Meta:
        model = MeterReadings

