import django_tables2 as tables
from . models import InvoicesCost

class InvoiceTable(tables.Table):
    class Meta:
        model = InvoicesCost
