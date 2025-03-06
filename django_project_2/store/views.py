from django.forms.models import model_to_dict
from django.http import HttpResponse
from .models import Category, Product
import json

# Create your views here.


def home_page(request):
    return HttpResponse("<h1> Store Page </h2>")


def ball(request):
    return HttpResponse("<p> price: 40$ </p>")


def category_data(request):
    data = Category.objects.all()
    data_list = {}
    for obj in data:
        if obj.parent_category:
            data_list.update({"category_name": obj.name, "parent_category": model_to_dict(obj.parent_category)})
        else:
            data_list.update({"category_name": obj.name, "parent_category": obj.parent_category})
    return HttpResponse(json.dumps(data_list), content_type='application/json')


def product_data(request):
    data = Product.objects.all()
    data_dict = []
    for obj in data:
        if obj. category:
            data_dict.append({"product name": obj.name, "parent category": [model_to_dict(i) for i in obj.category.all()]})
        else:
            data_dict.append({"product name": obj.name, "parent category": obj.category})
    return HttpResponse(json.dumps(data_dict), content_type="application/json")
