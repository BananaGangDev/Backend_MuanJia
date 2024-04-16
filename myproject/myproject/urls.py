from django.contrib import admin
from django.urls import path,include
from products import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/",include_docs_urls()),
    path('product/',include('products.urls')),
    path('order/',include('order.urls')),
    path('payment',include('payment.urls')),
]
