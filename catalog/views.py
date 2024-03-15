from django.shortcuts import render

from catalog.forms import ProductForm, CategoryForm
from catalog.models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:catalog")

    extra_context = {
        'some_text': "Какой-то текст для страницы добавления нового продукта",
        'title': "Новый продукт"
    }

    def form_valid(self, form):
        new_product = form.save()
        new_product.author = self.request.user
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'some_text': "Какой-то текст для страницы просмотра поста",
        'title': "Просмотр поста"
    }


class ProductListView(ListView):
    model = Product
    extra_context = {
        'some_text': "Какой-то текст для страницы товаров",
        'title': "Товары"
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(is_active=True)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    extra_context = {
        'some_text': "Какой-то текст для страницы изменения продукта",
        'title': "Отредактировать продукт"
    }


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:catalog")
    extra_context = {
        'some_text': "Какой-то текст для страницы удаления постов",
        'title': f"Удаляем пост "
    }



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


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("catalog:catalog")

    extra_context = {
        'some_text': "Какой-то текст для страницы добавления новой категории",
        'title': "Новая категория"
    }
