from django import forms
from django.forms.widgets import DateInput
from . models import MeterReadings, InvoicesCost

class MeterReadingsForm(forms.ModelForm):
    class Meta:
        model = MeterReadings
        fields = '__all__'

class InvoicesCostForm(forms.ModelForm):
    class Meta:
        model = InvoicesCost
        fields = '__all__'
        labels = {'invoice_number': 'Numer faktury',
                  'invoice_date': 'Data faktury',
                  'invoice_value': 'Wartość faktury brutto',
                  'invoice_type': 'Typ faktury',
                  'invoice_year_refers_to': 'Rok przypisania faktury',
                  'invoice_month_refers_to': 'Miesiąc przypisania faktury',
                  'invoice_status': 'Status faktury'}
        widgets = {'invoice_date': DateInput(attrs={'type': 'date'})}
        help_texts = {'invoice_number': '', 'invoice_type': '', 'invoice_status': ''}
