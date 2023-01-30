from django import forms
from . models import MeterReadings

class MeterReadingsForm(forms.ModelForm):
    class Meta:
        model = MeterReadings
        fields = '__all__'