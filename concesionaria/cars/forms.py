from django import forms
from cars.models import Comment, Review, Car, Sale
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from cars.models import Brand, Category
from django.utils.translation import gettext_lazy as _

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]
        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control', 'placeholder': _('Deja tu comentario'),}),
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
    price_gte = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':_('Precio Desde')}))
    price_lte = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':_('Precio Hasta')}))
    brand_id = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))
    used = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))
    category_id = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))
    year_gte = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':_('Año Desde')}))
    year_lte = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':_('Año Hasta')}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        brand_choices = [('0', _('Todos'))]
        brands = Brand.objects.all()
        for brand in brands:
            brand_choices.append((brand.id, brand.name))
        self.fields['brand_id'].choices = brand_choices

        used_choices = [('2', _('Todos')), ('0', _('Nuevo')), ('1', _('Usado'))]
        self.fields['used'].choices = used_choices

        category_choices = [('0', _('Todos'))]
        categories = Category.objects.all()
        for category in categories:
            category_choices.append((category.id, category.name))
        self.fields['category_id'].choices = category_choices

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
