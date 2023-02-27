import requests
from django.views.generic.edit import FormView, UpdateView
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from . models import MeterReadings, InvoicesCost, ElectricityMeter
from . forms import MeterReadingsForm, InvoicesCostForm, MeterFormSet, MeterReadingsChoicePeriod
from . tables import InvoiceTable, MeterReadingTable
from django_tables2 import RequestConfig

def MeterReadingsFormView(request):
    counters = ElectricityMeter.objects.all()
    initial_values = [{'name': counter.name} for counter in counters]
    option_form = MeterReadingsChoicePeriod(request.POST)

    if request.method == 'POST':
        formset = MeterFormSet(request.POST, initial=initial_values)
        test = option_form.cleaned_data['cost']

        formset.save()
        return render(request, 'success.html')
    else:
        formset = MeterFormSet(initial=initial_values)

    return render(request, 'energy/addmeterreadings.html', {'formset': formset, 'option_form': option_form})




class InvoicesCostFormView(FormView):
    template_name = 'energy/addinvoicecosts.html'
    form_class = InvoicesCostForm
    success_url = '/energy/invoice/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class InvoicesCostUpdateView(UpdateView):
    model = InvoicesCost
    template_name = 'energy/addinvoicecosts.html'
    form_class = InvoicesCostForm
    success_url = '/energy/invoice/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



def InvoiceView(request):

    invoices = InvoiceTable(InvoicesCost.objects.all().order_by('-invoice_year_refers_to', '-invoice_month_refers_to'))
    RequestConfig(request, paginate={"per_page": 25}).configure(invoices)
    context = {'invoices': invoices}
    return render(request, 'energy/invoice_list.html', context)

def MeterReadingsView(request):
    readings = MeterReadingTable(MeterReadings.objects.all())
    RequestConfig(request, paginate={"per_page": 25}).configure(readings)
    context = {'readings': readings}
    return render(request, 'energy/reading_list.html', context)

