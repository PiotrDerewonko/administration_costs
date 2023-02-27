from django import forms
from django.forms.widgets import DateInput
from . models import MeterReadings, InvoicesCost, ElectricityMeter

class MeterReadingsForm(forms.ModelForm):
    class Meta:
        model = MeterReadings
        fields = '__all__'
#todo dodac formularz dodwania danych recznie
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


class MeterReadingsFormTest(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'disabled': True}), label='name')
    class Meta:
        model = ElectricityMeter
        fields = ('id', 'name', 'test')
        labels = {'test': 'Wartość końcowa licznika'}
    test = forms.FloatField()


class MeterReadingsChoicePeriod(forms.Form):
    #todo tu zrobic aby automatycznie zaciagaly sie aktualne lata
    YEAR_CHOICES = [('2022', '2022'), ('2021', '2021')]
    MONTH_CHOICES = [(1, 'styczeń'), (2, 'luty'), (3, 'marzec'), (4, 'kwiecień'),
                     (5, 'maj'), (6, 'czerwiec'), (7, 'lipiec'), (8, 'sierpień'),
                     (9, 'wrzesień'), (10, 'październik'), (11, 'listopad'), (12, 'grudzień')]
    year_choices = forms.ChoiceField(choices=YEAR_CHOICES, label='Wybór roku')
    month_choices = forms.ChoiceField(choices=MONTH_CHOICES, label='Wybierz miesiąc')
    cost = forms.FloatField()

MeterFormSet = forms.modelformset_factory(ElectricityMeter, form=MeterReadingsFormTest, extra=0)
