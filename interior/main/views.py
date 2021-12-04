from django.shortcuts import get_object_or_404, render

from .models import Card, Group, Product


def searching(request, keyword):
    products = Product.objects.filter(title__contains=keyword)
    return render(request, 'main/catalog.html', {'products': products, 'keyword': keyword})

def index(request):
    offers = Product.objects.filter(old_price__gte=1)[:3]
    products = Product.objects.all()[:3]
    keyword = request.GET.get("q", None)
    if keyword:
        products = Product.objects.filter(title__contains=keyword)
        return render(request, 'main/catalog.html', {'products': products, 'keyword': keyword})
    context = {
        'offers': offers,
        'products': products,
        'keyword': keyword
    }
    return render(request, 'main/index.html', context)


def catalog(request):
    offers = Product.objects.filter(old_price__gte=1)
    products = Product.objects.all().order_by('price')
    keyword = request.GET.get("q", None)
    if keyword:
        products = Product.objects.filter(title__contains=keyword)
        return render(request, 'main/catalog.html', {'products': products, 'keyword': keyword})
    context = {
        'offers': offers,
        'products': products,
        'keyword': keyword
    }
    return render(request, 'main/catalog.html', context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    products = group.products.all()
    keyword = request.GET.get("q", None)
    if keyword:
        products = Product.objects.filter(title__contains=keyword)
        return render(request, 'main/catalog.html', {'products': products, 'keyword': keyword})
    context = {
        'group': group,
        'products': products,
        'keyword': keyword
    }
    return render(request, 'main/group.html', context)



def cart(request):
    products = Product.objects.all()[:10]
    cards = Card.objects.all()
    keyword = request.GET.get("q", None)
    if keyword:
        products = Product.objects.filter(title__contains=keyword)
        return render(request, 'main/catalog.html', {'products': products, 'keyword': keyword})
    context = {
        'products': products,
        'cards': cards,
        'keyword': keyword
    }
    return render(request, 'main/cart.html', context)