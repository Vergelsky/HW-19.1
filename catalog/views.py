from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def index(request):
    context = {
        'some_text': "Какой-то текст для главной страницы",
        'title': "Главная"
    }

    return render(request, 'catalog/index.html', context)


def contacts(request):
    context = {
        'some_text': "Какой-то текст для страницы контактов",
        'title': "Контакты"
    }

    return render(request, 'catalog/contacts.html', context)


def items(request):
    items_list = Product.objects.all()
    context = {
        'object_list': items_list,
        'some_text': "Какой-то текст для страницы товаров",
        'title': "Товары"
    }
    print(type(context['object_list'][0]))
    return render(request, 'catalog/items.html', context)
