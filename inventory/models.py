from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to="images")
    quantity = models.PositiveIntegerField(default=0)
    slug = models.SlugField(default="", null=False, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("view-product", args=[self.slug])

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Products"


class StockTransaction(models.Model):
    TRANSACTION_TYPES = [
        ("IN", "Stock In"),
        ("OUT", "Stock Out")
    ]

    transaction_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    transaction_date = models.DateField(auto_now_add=True)
    remarks = models.CharField(max_length=250)
    product = models.ForeignKey(Product, related_name="transactions", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Transactions"

    def delete(self, *args, **kwargs):
        product = self.product

        if self.type == "IN":
            product.quantity -= self.quantity
        elif self.type == "OUT":
            product.quantity += self.quantity
        product.save()

        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.transaction_name} - {self.type}"



