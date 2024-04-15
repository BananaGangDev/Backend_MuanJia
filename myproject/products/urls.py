from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_all,name='Product'),
    path('name/<str:search_name>',views.get_by_product_name,name='Product'),
    path('id/<int:id>',views.get_by_id,name="Product"),
]

