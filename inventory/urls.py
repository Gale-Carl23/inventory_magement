from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("products", views.ProductsViewList.as_view(), name="all-products"),
    path("products/api", views.view_products_api, name="all-products-api"),
    path("product/<slug:slug>", views.view_product, name="view-product")
]
