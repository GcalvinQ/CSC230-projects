from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib import messages

# Create your views here.
@login_required(login_url='user-login')
def index(request):
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    staff = User.objects.filter()
    staff_count = staff.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.staff = request.user
            obj.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'order': order,
        'product': product,
        'product_count': product_count,
        'order_count': order_count,
        'staff_count': staff_count,
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):
    return render(request, 'dashboard/staff.html')

login_required(login_url='user-login')
def product(request):
    product = Product.objects.all()
    product_count = product.count()
    staff = User.objects.filter()
    staff_count = staff.count()
    order = Order.objects.all()
    order_count = order.count()
    product_quantity = Product.objects.filter(name='')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'product': product,
        'form': form,
        'staff_count': staff_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/product.html', context)

@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin1'])
def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
         product.delete()
         return redirect('dashboard-product')
    context = {
        'product': product
    }
    return render(request, 'dashboard/product_delete.html', context)

@login_required(login_url='user-login')
def order(request):
    order = Order.objects.all()
    order_count = order.count()
    staff = User.objects.filter()
    staff_count = staff.count()
    product = Product.objects.all()
    product_count = product.count()

    context = {
        'order': order,
        'staff_count': staff_count,
        'product_count': product_count,
        'order_count': order_count,
        'staff': staff
    }
    return render(request, 'dashboard/order.html', context)
def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
         order.delete()
         return redirect('dashboard-order')
    context = {
        'order': order
    }
    return render(request, 'dashboard/orders_delete.html', context)
