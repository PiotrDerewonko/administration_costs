from django.urls import path
from . import views

urlpatterns = [path('test/', views.MeterReadingsFormView.as_view()),
               path('test2/', views.FormSuccessView.as_view(), name = 'form_success'),
               path('invoice/', views.InvoiceView, name='invoice_list')]