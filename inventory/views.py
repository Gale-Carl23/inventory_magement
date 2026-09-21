from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from .models import Product
from django.http import HttpResponseRedirect, JsonResponse
from .forms import TransactionForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm

# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "inventory/register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "inventory/register.html", {"form": form})

class ProductsViewList(ListView):
    template_name = "inventory/view_all_products.html"
    model = Product
    context_object_name = "products"

class TransactionView(LoginRequiredMixin, View):
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
           
            transaction.user = request.user
            product = transaction.product
            if product.quantity >= transaction.quantity:
                if transaction.type == "IN":
                    product.quantity += transaction.quantity
                elif transaction.type == "OUT":
                    product.quantity -= transaction.quantity

                product.save()
                transaction.save()
                return HttpResponseRedirect("/create-transaction")
            else:
                posted_form.add_error(
                "quantity",
                f"Not enough stock. Available quantity: {product.quantity}"
            )
                return render(request, "inventory/create_transaction.html", {"form": posted_form})
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

