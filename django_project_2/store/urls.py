from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page),
    path("ball/", views.ball),
    path("category_data/", views.category_data),
    path("product_data/", views.product_data)
]
