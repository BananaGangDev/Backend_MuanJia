from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_all,name='Get Product'),
    path('name/<str:search_name>',views.get_by_product_name,name='Get Product By Product Name'),
    path('id/<int:id>',views.get_product_by_id,name="Get Product By Product ID"),
]

