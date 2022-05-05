from django.contrib import admin
from . import models

admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Item)
admin.site.register(models.Vendor)
admin.site.register(models.VendorItems)

