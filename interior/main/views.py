from django.shortcuts import get_object_or_404, render

from .models import Card, Group, Product


def index(request):
    offers = Product.objects.filter(old_price__gte=1)[:3]
    products = Product.objects.all()[:3]
    context = {
        'offers': offers,
        'products': products,
    }
    return render(request, 'main/index.html', context)


def catalog(request):
    offers = Product.objects.filter(old_price__gte=1)
    products = Product.objects.all().order_by('price')
    context = {
        'offers': offers,
        'products': products,
    }
    return render(request, 'main/catalog.html', context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    products = group.products.all()
    context = {
        'group': group,
        'products': products,
    }
    return render(request, 'main/group.html', context)



def cart(request):
    products = Product.objects.all()[:10]
    cards = Card.objects.all()
    context = {
        'products': products,
        'cards': cards,
    }
    return render(request, 'main/cart.html', context)