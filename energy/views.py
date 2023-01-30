from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from . models import MeterReadings, InvoicesCost
from . forms import MeterReadingsForm
from . tables import InvoiceTable
from django_tables2 import RequestConfig

class MeterReadingsFormView(FormView):
    template_name = 'energy/addmeterreadings.html'
    form_class = MeterReadingsForm
    success_url = '/energy/test2/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("zapisane")

def InvoiceView(request):
    ATTRIBUTES = {
        "th": {
            "_ordering": {
                "orderable": "sortable",  # Instead of `orderable`
                "ascending": "ascend",  # Instead of `asc`
                "descending": "descend"  # Instead of `desc`
            }
        }
    }
    invoices = InvoiceTable(InvoicesCost.objects.all())
    RequestConfig(request).configure(invoices)
    #invoices.order_by = ['invoice_year_refers_to', 'invoice_month_refers_to']
    context = {'invoices': invoices}
    return render(request, 'energy/invoice_list.html', context)