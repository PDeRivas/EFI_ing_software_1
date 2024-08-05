from django import forms
from cars.models import Comment, Review
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'text',
            'rating',
        ]

        widgets = {
            'rating': forms.NumberInput(attrs={'step':'1', 'min':'1', 'max':'10'}),
        }