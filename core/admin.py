from django.contrib import admin
from .models import OrderItem, VendorItems, Vendor, Item, Order

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Item)
admin.site.register(Vendor)
admin.site.register(VendorItems)
