from django.urls import path
from . import views

urlpatterns = [

    path('vendorItems/', views.VendorItemsList.as_view()),
    path('vendor/', views.VendorList.as_view()),
    path('item/', views.ItemList.as_view()),
    path('<int:pk>/CreateOrderItem/', views.CreateOrderItem.as_view(), name='create_order_item'),
    path('CreateVendorItem', views.CreateVendorItem.as_view()),
    path('CreateVendor', views.CreateVendor.as_view()),
    path('CreateItem', views.CreateItem.as_view()),
    path('OrderList', views.OrderList.as_view(),),
    path('createOrder', views.CreateOrder.as_view()),
    path('<pk>/deleteOrder', views.DeleteOrder.as_view(), name='delete_order'),
    path('<pk>/updateOrder', views.UpdateOrder.as_view(), name='update_order'),
    path('<pk>/deleteOrderItem', views.DeleteOrderItem.as_view(), name='delete_order_item'),
    path('<pk>/updateOrderItem', views.UpdateOrderItem.as_view(), name='update_order_item'),
    path('<pk>/deleteVendorItems', views.DeleteVendorItem.as_view(), name='delete_vendor_items'),
    path('<pk>/updateVendorItems', views.UpdateVendorItem.as_view(), name='update_vendor_items'),
    path('<pk>/deleteVendor', views.DeleteVendor.as_view(), name='delete_vendor'),
    path('<pk>/updateVendor', views.UpdateVendor.as_view(), name='update_vendor'),
    path('<pk>/deleteItem', views.DeleteItem.as_view(), name='delete_item'),
    path('<pk>/updateItem', views.UpdateItem.as_view(), name='update_item'),
    path('<pk>/ViewOrderItem', views.ViewOrderItem.as_view(), name='view_order_item'),
    path('<pk>/CreateTest', views.CreateTest.as_view())

]


