from django.urls import path
from . import views

urlpatterns = [path('addmeterread/', views.MeterReadingsFormView),
               path('addinvoicecosts/', views.InvoicesCostFormView.as_view()),
               path('updateinvoicecosts/<int:pk>', views.InvoicesCostUpdateView.as_view(), name='edit_cost'),
               path('invoice/', views.InvoiceView, name='invoice_list'),
               path('readings/', views.MeterReadingsView, name='readings_list')]