from django.urls import path
from . import views

urlpatterns = [path('addmeterread/', views.MeterReadingsFormView.as_view()),
               path('addmeterreadsucc/', views.FormSuccessView.as_view(), name = 'form_success'),
               path('invoice/', views.InvoiceView, name='invoice_list'),
               path('readings/', views.MeterReadingsView, name='readings_list')]