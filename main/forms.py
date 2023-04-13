from django import forms

class UpdatePriceForm(forms.Form):
    price = forms.DecimalField(label='Новая цена', decimal_places=2, max_digits=8)
    quantity_in_stock = forms.DecimalField(label="Нова кількість на складі")