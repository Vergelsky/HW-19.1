from django import forms

from blog.models import Blog, Version


class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('blog_title', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def cleaning(self, models_field):
        # Вспомогательный метод для валидатора. Он делает всю работу.

        exception_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        cleaned_data = self.cleaned_data.get(models_field)

        for exc_word in exception_words:
            if exc_word in cleaned_data or exc_word.capitalize() in cleaned_data or exc_word.upper() in cleaned_data:
                raise forms.ValidationError('Использовано запрещённое слово')

        return cleaned_data

    def clean_blog_title(self):
        # валидатор просто передаёт имя нужного поля
        return self.cleaning('blog_title')


    def clean_content(self):
        # валидатор просто передаёт имя нужного поля

        return self.cleaning('content')


class VersionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():

                field.widget.attrs['class'] = 'form-control ms-5'

    class Meta:
        model = Version
        fields = ('version_title', 'product', 'version_number', 'is_current')