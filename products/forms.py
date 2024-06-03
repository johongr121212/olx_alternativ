from .models import Product
from django import forms


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'category', 'address',
            'phone_number', 'tg_username','image')
        
    def save(self,request,commit=True):
        product = self.instance
        product.author = request.user
        super().save(commit)
        return product
    
class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'category',
                'address','phone_number','tg_username','image')