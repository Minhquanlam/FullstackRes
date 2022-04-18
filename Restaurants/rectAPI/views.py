from django import forms
from django.shortcuts import redirect, render
from rectAPI.models import order, pizza, drink, hamburger
from django.http import HttpResponse
from .forms import OrderForm
#from rectAPI.serializers import PizzaSerializer
import json
# Create your views here.
def index(request):
    return render(request, "first.html")

def payment(request):
    return render(request, "payment.html")


def pizzas(request):
    items = pizza.objects.all().values()

    items_list = list(items)

    data = json.dumps(items_list)
    return HttpResponse(data, content_type="application/json")

def drinks(request):
    items = drink.objects.all().values()

    items_list = list(items)

    data = json.dumps(items_list)
    return HttpResponse(data, content_type="application/json")

def hamburgers(request):
    items = hamburger.objects.all().values()

    items_list = list(items)

    data = json.dumps(items_list)
    return HttpResponse(data, content_type="application/json")

