from django.urls import path
from . import views

urlpatterns = [
    # path('create',views.create_payment,name='Create Payment'),
    path('get_payment_by_payment_id/<str:id>',views.get_payment_by_id,name='Get Payment By Payment_id'),
    path('<str:id>/<path:image>',views.update_status,name="Update Payment"),
    path('get_payment_by_order_id/<str:id>',views.get_payment_by_order_id,name='Get Payment By Order_id')
]
