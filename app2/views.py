from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def tura(request):
    return HttpResponse('it is a boy name')

def ture(request):
    return HttpResponse('it is a girl name')
    