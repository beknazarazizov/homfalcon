from django.shortcuts import render, redirect

from customer.forms import CustomerModelForm
from customer.models import Customer


# Create your views here.

def customer_list(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request,'customer/customer_list.html',context)

def add_customer(request):
    form=CustomerModelForm()
    if request.method == 'POST':
        form=CustomerModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customers')
    context={'form':form}
    return render(request,'customer/add_customer.html',context)

def delete_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    if customer:
        customer.delete()
        return redirect('customers')



