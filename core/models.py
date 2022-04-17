from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    name = models.CharField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_created_order', null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_updated_order', null=True)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_approved_order', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'order'


class OrderItem(models.Model):
    total_price = models.FloatField(default='0', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_created_orderitem', null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_updated_orderitem', null=True)
    vendor_items = models.ForeignKey('VendorItems', on_delete=models.CASCADE, related_name='vendoritem', null=True)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitem_order', null=True)

    @property
    def item_price(self):
        return self.quantity * self.vendor_items.price


class Item(models.Model):
    name = models.CharField(max_length=64, unique=True)
    type = models.CharField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_created_item')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_updated_item', null=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=64, unique=True)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    address = models.CharField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_created_vendor', null=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_updated_vendor', null=True)

    def __str__(self):
        return self.name


class VendorItems(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor_VendorItem', default='',
                               null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_vendoritems', default='', null=True)
    price = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_created_vendoritems', null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_updated_vendoritems', null=True)

    def __str__(self):
        return self.item.name
