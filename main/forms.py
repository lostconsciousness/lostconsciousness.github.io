from django import forms

class UpdatePriceForm(forms.Form):
    choices = [
        ('True', 'Так'),
        ('False', 'Hі'),
    ]
    price = forms.DecimalField(label='Новая цена', decimal_places=2, max_digits=8,required=False)
    quantity_in_stock = forms.DecimalField(label="Нова кількість на складі", required=False)
    available = forms.ChoiceField(label="Наявність",widget=forms.RadioSelect, choices=choices)