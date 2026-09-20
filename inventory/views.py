from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product
from django.http import HttpResponseRedirect, JsonResponse
from .forms import TransactionForm
from django.views import View

# Create your views here.
class ProductsViewList(ListView):
    template_name = "inventory/view_all_products.html"
    model = Product
    context_object_name = "products"

class TransactionView(View):
    def get(self, request):
        print("GET CALLED")
        transaction_form = TransactionForm()
        return render(request, "inventory/create_transaction.html", {
            "form": transaction_form
        })

    def post(self, request):
        posted_form = TransactionForm(request.POST)
        print("POSTED VALID", posted_form.is_valid())
        if posted_form.is_valid():
            transaction = posted_form.save(commit=False)
           

            product = transaction.product
            print("BEFORE", product.quantity)

            if transaction.type == "IN":
                product.quantity += transaction.quantity
            elif transaction.type == "OUT":
                product.quantity -= transaction.quantity

            product.save()
            transaction.save()
            print("AFTER", product.quantity)
            return HttpResponseRedirect("/create-transaction")
        else:
            print("INVALID")
    
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

