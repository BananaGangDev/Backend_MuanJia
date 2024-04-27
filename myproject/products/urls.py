from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_all,name='Get Product'),
    path('name/<str:search_name>',views.get_by_product_name,name='Get Product By Product Name'),
    path('id/<str:id>',views.get_product_by_id,name="Get Product By Product ID"),
    path('get_price_by_id/<str:id>',views.get_price_by_id,name="Get Price By Product ID"),
    path('get_soud/<str:id>',views.get_sound,name="Get Sound By ID")
]

