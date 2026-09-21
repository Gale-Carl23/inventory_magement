from django import forms
from .models import StockTransaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TransactionForm(forms.ModelForm):
    class Meta:
        model = StockTransaction
        fields = ["transaction_name", "type", "quantity", "remarks", "product"]
        

        labels = {
            "transaction_name": "Name of transaction",
            "transaction_date": "Date of transaction",
            "remarks": "Your remarks",
        }
        error_messages = {
            "transaction_name": {
                "required": {"You must provide a name here."},
                "max_length": {"Character limit."}
            }
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]