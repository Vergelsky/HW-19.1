from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.utils.text import slugify

from blog.models import Blog, Version
from blog.forms import PostForm, VersionForm


def rus_to_slug(rus_string):
    """
    Превращает текст в слаг, переводя русские буквы в транслит
    :param rus_string: текст для слагирования
    :return: слаг, готовый для вставки в url
    """

    rus_abc = ('абвгдеёжзийклмнопрстуфхцчшщьыъэюя')
    slug_abc = ('a', 'b', 'v', 'g', 'd', 'e', 'jo', 'zh', 'z', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f',
                'h', 'c', 'ch', 'sh', 'sch', '', 'y', '', 'e', 'ju', 'ja')
    trance_table = {}
    for num in range(len(rus_abc)):
        letter = rus_abc[num]
        trance_table[ord(letter)] = slug_abc[num]

    result = rus_string.lower().translate(trance_table)

    return slugify(result)


class FormValidMixin():
    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = rus_to_slug(new_post.blog_title)
            new_post.save()
        return super().form_valid(form)


class BlogCreateView(FormValidMixin, CreateView):
    model = Blog
    form_class = PostForm
    success_url = reverse_lazy("blog:blog")



    extra_context = {
        'some_text': "Какой-то текст для страницы добавления нового поста",
        'title': "Новый пост"
    }

    # def get_success_url(self):
    #     return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'some_text': "Какой-то текст для страницы просмотра постов",
        'title': "Наш блог"
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {
        'some_text': "Какой-то текст для страницы просмотра поста",
        'title': "Просмотр поста"
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(FormValidMixin, UpdateView):
    template_name = 'blog/blog_update.html'
    model = Blog
    form_class = PostForm
    # success_url = reverse_lazy("blog:blog")
    extra_context = {
        'some_text': "Какой-то текст для страницы изменения постов",
        'title': f"Отредактировать пост"
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        VersionFormset = inlineformset_factory(Blog, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']

        if formset.is_valid():
            formset.instance = form.save()
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.object.slug])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog")
    extra_context = {
        'some_text': "Какой-то текст для страницы удаления постов",
        'title': f"Удаляем пост \"\""
    }


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy("blog:blog")

    extra_context = {
        'some_text': "Какой-то текст для страницы добавления новой версии",
        'title': "Новая версия"
    }



