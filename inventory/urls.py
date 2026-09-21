from . import views
from django.urls import path
from django.contrib.auth import view as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("products", views.ProductsViewList.as_view(), name="all-products"),
    path("products/api", views.view_products_api, name="all-products-api"),
    path("product/<slug:slug>", views.view_product, name="view-product"),
    path("create-transaction", views.TransactionView.as_view(), name="create-transaction")
]
