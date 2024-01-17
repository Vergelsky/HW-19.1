from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content')
    success_url = reverse_lazy("blog:blog")
    extra_context = {
        'some_text': "Какой-то текст для страницы добавления нового поста",
        'title': "Новый пост"
    }


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'some_text': "Какой-то текст для страницы просмотра постов",
        'title': "Наш блог"
    }


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {
        'some_text': "Какой-то текст для страницы просмотра поста",
        'title': f"Пост \"\""
    }


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content')
    success_url = reverse_lazy("blog:blog")
    extra_context = {
        'some_text': "Какой-то текст для страницы изменения постов",
        'title': f"Отредактировать пост \"\""
    }

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog")
    extra_context = {
        'some_text': "Какой-то текст для страницы удаления постов",
        'title': f"Удаляем пост \"\""
    }