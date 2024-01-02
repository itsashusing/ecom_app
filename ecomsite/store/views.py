from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.views import _cart_id
from cart.models import CartItem, Cart

from django.core.paginator import Paginator
# Create your views here.


def home(request, category_slug=None):
    products = None
    categories = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    paginator = Paginator(products, 4)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'products': products,
        'product_count': product_count,
        'page_obj': page_obj
    }
    return render(request, 'store/index.html', context)


def product_details(request, category_slug, product_slug):
    try:
        product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(
            cart__cart_id=_cart_id(request), product=product).exists()
    except:
        raise Exception

    context = {
        'product': product,
        'in_cart': in_cart
    }
    return render(request, 'store/product_details.html', context)
