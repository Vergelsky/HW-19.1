from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def items(request):
    items_list = Product.objects.all()
    context = {
        'object_list': items_list
    }
    print(type(context['object_list'][0]))
    return render(request, 'catalog/items.html', context)
