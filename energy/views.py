from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view(request):
    m = '<h1>test</h1>'
    return HttpResponse(m)
