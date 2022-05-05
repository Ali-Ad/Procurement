from django import forms
from django.forms import modelformset_factory, inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from . import models


class OrderItemForm(forms.ModelForm):
    # quantity = forms.IntegerField(min_value=1)
    # order = forms.ModelChoiceField(queryset=models.Order.objects.all())
    # vendor_item = forms.ModelChoiceField(models.Order.objects.all())

    class Meta:
        model = models.OrderItem
        fields = ['order', 'vendor_items', 'quantity']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('order', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         ),
    #         Row(
    #             Column('vendor_items', css_class='form-group col-md-7 mb-0')
    #
    #         ), 'quantity',
    #         Submit('submit', 'save')
    #     )


OrderItemFormset = modelformset_factory(models.OrderItem, fields=('vendor_items', 'quantity'), extra=1, )




class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ['name', 'type']


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['name']


OrderFormset = modelformset_factory(models.Order, fields=('name',), extra=1)


class VendorForm(forms.ModelForm):
    class Meta:
        model = models.Vendor
        fields = ['name', 'phone', 'email', 'address']


class VendorItemsForm(forms.ModelForm):
    class Meta:
        model = models.VendorItems
        fields = ['vendor', 'item', 'price']
