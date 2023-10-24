from django import forms
from django.forms import Textarea, EmailInput, TextInput
from django.utils.translation import gettext_lazy as _

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('author', 'service', 'text', 'phone_number', 'e_mail',)
        widgets = {
            'text': Textarea(attrs={'style': 'width: 100%;', 'rows': 5, 'placeholder': 'Текст заявки'},),
            'e_mail': EmailInput(attrs={'style': 'width: 100%;', 'placeholder': 'test@example.com'}),
            'phone_number': TextInput(attrs={'style': 'width: 100%;', 'placeholder': '+79785558989'}),
            'author': TextInput(attrs={'style': 'width: 100%;', 'placeholder': 'Имя'}),          
        }
        # labels = {
        #     "service": _(""),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].empty_label = "Услуга не выбрана"