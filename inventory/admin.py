from django.contrib import admin
from .models import Product, Category, StockTransaction

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("category",)
    list_display = ("name", "price")

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(StockTransaction)