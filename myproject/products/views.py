from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
import pyrebase
import json
from myproject.connections import global_db
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError,ParseError
from rest_framework import status
import requests


@api_view(['GET'])
def get_all(request):
    if request.method == 'GET':
        products_db = global_db.get_db('products').stream()
        products = {}
        for product in products_db:
            # print(product.id,product.to_dict())
            product_id = str(product.id)
            product_item = product.to_dict()
            products.update({product_id : product_item})
        # print(products)
        return Response(data=products,status=status.HTTP_200_OK)
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])    
def get_by_product_name(request,search_name):
    if request.method == 'GET':
        result = []
        for product in global_db.get_db('products').stream():
            product_id = product.id
            product_item = product.to_dict()
            if search_name in product_item['product_name']:
                result.append({product_id:product_item})
            
        if not result :
            return Response(data="No data. Please refill again.",status=status.HTTP_204_NO_CONTENT)
        else :              
            return Response(result,status=status.HTTP_200_OK)
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])    
def get_product_by_id(request,id):
    # print(id,type(id))
    if request.method == 'GET':
        product = global_db.get_db('products').document(str(id)).get()
        result = []
        if product :
            product_id = product.id
            product_item = product.to_dict()
            result.append({product_id:product_item})
            return Response(result,status=status.HTTP_200_OK)   
        else:
            return Response(data="No data. Please refill again.",status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
def get_price_by_id(id):
    return float(global_db.get_db('products').document(str(id)).get().to_dict()['price'])
    
    # for key,value in global_db.get_db('products').items():
    #     if  id == int(key):
    #         # print(value['price'],type(value['price']))
    #         return float(value['price'])
    
