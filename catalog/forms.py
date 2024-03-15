from django import forms

from catalog.models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_description', 'category', 'image', 'price', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            from django.forms import CheckboxInput
            if isinstance(field.widget, CheckboxInput):

                field.widget.attrs['class'] = 'form-check'

            else:
                field.widget.attrs['class'] = 'form-control'


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            from django.forms import CheckboxInput
            if isinstance(field.widget, CheckboxInput):

                field.widget.attrs['class'] = 'form-check'

            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Category
        fields = ('category_name', 'category_description')
