from django.urls import path
from . import views

urlpatterns = [path('addmeterread/', views.MeterReadingsFormView.as_view()),
               path('addinvoicecosts/', views.InvoicesCostFormView.as_view()),
               path('invoice/', views.InvoiceView, name='invoice_list'),
               path('readings/', views.MeterReadingsView, name='readings_list')]