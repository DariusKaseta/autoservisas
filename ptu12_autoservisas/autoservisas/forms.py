from django import forms
from . import models

class OrderReviewForm(forms.ModelForm):
    class Meta:
        model = models.UserOrderReview
        fields = ("content", "order", "reviewer")
        widgets = {
            "order" : forms.HiddenInput(),
            "reviewer" : forms.HiddenInput(),
        }