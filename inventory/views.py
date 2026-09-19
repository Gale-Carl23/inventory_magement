from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product
from django.http import JsonResponse

# Create your views here.
class ProductsViewList(ListView):
    template_name = "inventory/view_all_products.html"
    model = Product
    context_object_name = "products"

    
def index(request):
    return render(request, "inventory/index.html")

def view_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "inventory/view_product.html",{
        "product": product
    })

def view_products_api(request):
    products = list(Product.objects.values())
    return JsonResponse(
        products, safe=False
    )

