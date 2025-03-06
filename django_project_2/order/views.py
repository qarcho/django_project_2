from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request, order):
    return render(request, "order/main.html", {"order": order})


def order_list(request):
    return HttpResponse("<h2>order</h2>")