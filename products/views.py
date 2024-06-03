from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from .forms import NewProductForm,ProductUpdateForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Product,Comment
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import ListView
from django.db.models import Q
from users.models import Saved

# Create your views here.
def create_product(request):
    if request.method == 'POST':
        form = NewProductForm(data = request.POST, files=request.FILES)
        if form.is_valid():
            form.save(request)
            messages.success(request,"Successfully created")
            return redirect('main:index')
    else:
        form = NewProductForm()
    return render(request, 'product_new.html', {'form': form})

def product_details(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    
    context = {
        
        'product': product
    }
    
    return render(request, 'product_details.html',context)
    
def product_update_view(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    if request.method == 'POST':
        form = ProductUpdateForm(data=request.POST, instance=product, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('main:index')
    else:
        form = ProductUpdateForm()
        
    return render(request, 'product_update.html', {'form':form, 'product': product})


def product_delete_view(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    product.delete()
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

class SearchView(ListView):
    model = Product
    template_name = 'search.html'
    context_object_name = 'search_result'
    
    def get_queryset(self):
        data = self.request.GET.get('q')
        natija = Product.objects.filter(
            Q(title__icontains=data)
        )
        
        return natija
    
def add_saved(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    Saved.objects.create(product=product, author=request.user)
    
    return redirect('main:index')


def get_saved_products(request):
    saved_products = Saved.objects.all()
    context = {
        'products': saved_products
    }

    return render(request, 'saved.html', context)


def new_comment(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    if request.method == 'POST':
        Comment.objects.create(
            author=request.user,
            product = product,
            body = request.POST['body']
        )
        messages.info(request, "Successfully created")
        return redirect('product_details', product_id)
    return HttpResponse("add comment")

def delete_comment(request, product_id, comment_id):
    comment = get_object_or_404(Comment,id=comment_id)
    if request.user == comment.author:
        comment.delete()
        messages.info(request, "Successfully deleted")
        return redirect('product_details', product_id)