
from .views import *
from django.urls import path

urlpatterns = [
    path("", product_list, name = "product_list_url"),
    path("cat/ ", category_list, name = "category_list_url"),
    path("product/<int:pk>/", product_detail, name = "product_detail_url"),
    path("cat/<int:pk>/",category_detail, name = "category_detail_url"),
    path("save_order", save_order),
]
