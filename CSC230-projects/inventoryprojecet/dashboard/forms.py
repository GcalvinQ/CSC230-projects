from django import forms
from .models import Product, Order

#Product form
class ProductForm(forms.ModelForm):    
    class Meta:
        model = Product        
        fields = ['name']

#Order form
class OrderForm(forms.ModelForm):    
    class Meta:
        model = Order        
        fields = ['name']