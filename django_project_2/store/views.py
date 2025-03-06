from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product
from django.core import serializers

# Create your views here.


def home_page(request):
    return HttpResponse("<h1> Store Page </h2>")


def ball(request):
    return HttpResponse("<p> price: 40$ </p>")


def category_data(request):
    data = Category.objects.all()
    data_in_json = serializers.serialize("json", data)
    return HttpResponse(data_in_json, content_type="application/json")


def product_data(request):
    all_objects = Product.objects.all()
    parent_categories = Category.objects.filter(product__isnull=False)
    data_in_json = serializers.serialize("json", [*all_objects, *parent_categories])

    return HttpResponse(data_in_json, content_type="application/json")
