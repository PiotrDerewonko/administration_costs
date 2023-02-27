import django_tables2 as tables
from django_tables2.utils import A
from . models import InvoicesCost, MeterReadings


class InvoiceTable(tables.Table):
    invoice_number = tables.LinkColumn("edit_cost", args=[A("pk")])

    class Meta:
        model = InvoicesCost
        template_name = "django_tables2/bootstrap-responsive.html"


class MeterReadingTable(tables.Table):
    id = tables.LinkColumn("invoice_list")
    class Meta:
        model = MeterReadings

        template_name = "django_tables2/bootstrap-responsive.html"

