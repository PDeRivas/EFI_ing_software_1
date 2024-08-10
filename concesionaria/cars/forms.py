from django import forms
from cars.models import Comment, Review, Car, Sale
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from cars.models import Brand, Category

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]
        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Deja tu comentario',}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'text',
            'rating',
        ]

        widgets = {
            'rating': forms.NumberInput(attrs={'step':'1', 'min':'1', 'max':'10'}),
            'text': forms.Textarea(attrs={'class':'form-control'}),
        }

class FilterForm(forms.Form):
    brand_choices = [('0', 'Todos')]
    brands = Brand.objects.all()
    for brand in brands:
        brand_choices.append((brand.id, brand.name))

    used_choices = [('2', 'Todos'),('0', 'Nuevo'),('1', 'Usado')]

    category_choices = [('0', 'Todos')]
    categorys = Category.objects.all()
    for category in categorys:
        category_choices.append((category.id, category.name))

    price_gte = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio Desde'}))
    price_lte = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio Hasta'}))
    brand_id = forms.ChoiceField(choices=brand_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    used = forms.ChoiceField(choices=used_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    category_id = forms.ChoiceField(choices=category_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    year_gte = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Año Desde'}))
    year_lte = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Año Hasta'}))

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = [
            'credit_card_number',
            'country',
            'city',
            'postal_code',
            'phone',
        ]

        widgets = {
            'credit_card_number': forms.NumberInput(attrs={'step':'1', 'class':'form-control'}),
            'country': forms.Select(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'postal_code': forms.NumberInput(attrs={'step':'1', 'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'step':'1', 'class':'form-control'}),
        }
