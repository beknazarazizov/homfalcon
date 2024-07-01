from django.shortcuts import render, redirect

from app.models import Product


# Create your views here.

def index(request):
    products = Product.objects.all().order_by('-id')[:4]
    context = {'products': products}
    return render(request,'app/index.html',context)

def product_details(request,pk):
    product = Product.objects.get(id=pk)
    atributes=product.get_attributes()
    context = {'product':product,'atributes':atributes}
    return  render(request,'app/product_detail.html',context)

# def add_product(request):
#     form = ProductModelForm()
#     if request.method == 'POST':
#         form = ProductModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     context = {
#         'form': form,
#     }
#     return render(request, 'app/add-product.html', context)
from app.forms import ProductModelForm
def add_product(request):
    form=ProductModelForm()
    if request.method == 'POST':
        form=ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request,'app/add_product.html',context)

