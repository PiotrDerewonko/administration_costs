from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from . models import MeterReadings, InvoicesCost
from . forms import MeterReadingsForm
from . tables import InvoiceTable, MeterReadingTable
from django_tables2 import RequestConfig

class MeterReadingsFormView(FormView):
    template_name = 'energy/addmeterreadings.html'
    form_class = MeterReadingsForm
    success_url = '/energy/addmeterreadsucc/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("zapisane")

def InvoiceView(request):

    invoices = InvoiceTable(InvoicesCost.objects.all().order_by('-invoice_year_refers_to', '-invoice_month_refers_to'))
    RequestConfig(request, paginate={"per_page": 25}).configure(invoices)
    context = {'invoices': invoices}
    return render(request, 'energy/invoice_list.html', context)

def MeterReadingsView(request):
    readings = MeterReadingTable(MeterReadings.objects.all())
    RequestConfig(request).configure(readings)
    context = {'readings': readings}
    return render(request, 'energy/reading_list.html', context)

