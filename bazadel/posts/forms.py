from django import forms
from django.forms import Textarea

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('author', 'service', 'text', 'phone_number', 'e_mail',)
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].empty_label = "Услуга не выбрана"