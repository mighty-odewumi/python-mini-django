from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    # products = Product.objects.all()
    return render(request, 'index.html',
                  )


def prod(request):
    products = Product.objects.all()
    return render(request, 'product.html',
                  {'products': products})

def cart(request):

    return HttpResponse('Product added to your cart.')


"""
def newproducts(request):
    return HttpResponse('These are new products to be displayed.')
"""

