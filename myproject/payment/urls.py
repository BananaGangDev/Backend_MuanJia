from django.urls import path
from . import views

urlpatterns = [
    path('create',views.create_payment,name='Create Payment'),
    path('get_payment_by_payment_id/<int:id>',views.get_payment_by_id,name='Get Payment By Payment_id'),
    path('update_status',views.update_status,name="Update Payment"),
    path('get_payment_by_order_id/<int:id>',views.get_payment_by_order_id,name='Get Payment By Order_id')
]

