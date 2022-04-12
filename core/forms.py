from django import forms
from django.forms import modelformset_factory

from . import models


class OrderItemForm(forms.ModelForm):

    class Meta:
        model = models.OrderItem
        fields = ['name', 'order', 'vendor_items', 'quantity']


OrderItemFormset = modelformset_factory(models.OrderItem, fields=('vendor_items', 'quantity'), extra=1,)


class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ['name', 'type']


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['name']


OrderFormset = modelformset_factory(models.Order, fields=('name', ), extra=1)


class VendorForm(forms.ModelForm):
    class Meta:
        model = models.Vendor
        fields = ['name', 'phone', 'email', 'address']


class VendorItemsForm(forms.ModelForm):
    class Meta:
        model = models.VendorItems
        fields = ['vendor', 'item', 'price']
