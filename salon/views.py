from django.shortcuts import render
from Products.models import  Types, Brands
from ReceiptsExpenses.models import SpentProducts, ReceiveProducts
from django.http import HttpResponse

# Create your views here.
def GetMostPopular (request):
    return (HttpResponse("AAAAAA"))

