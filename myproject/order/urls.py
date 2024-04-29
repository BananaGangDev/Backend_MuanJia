from django.urls import path
from . import views

urlpatterns = [
    path('order',views.get_all_order,name='Get Order'),
    path('order_items',views.get_all_order_items,name='Get Order_items'),
    path('order_id/<str:id>',views.get_order_by_id,name='Get Order by Order_id'),
    path('order_item_id/<str:order_id>',views.get_order_item_by_id,name="Get Order_items By Order_id "),
    path('create/<str:firstname>/<str:lastname>/<str:phone>/<str:email>/<str:address>/<str:payment_channel>/<str:items>',views.create_order,name="Create Order"),
]

#format item = {product_id:quantity} แล้ว dump ส่งมาเป็น str