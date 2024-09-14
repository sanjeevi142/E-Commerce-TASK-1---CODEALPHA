from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def product_list(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        products = list(Product.objects.values())
        return JsonResponse(products, safe=False)
    return render(request, 'store/index.html')

def cart_view(request):
    # This is where you handle the cart logic
    return render(request, 'store/cart.html')

def product_list(request):
    # This view should render the product list page
    return render(request, 'store/products.html')

def home(request):
    return render(request, 'store/index.html')