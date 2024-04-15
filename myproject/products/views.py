from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
import pyrebase
import json
from myproject.connections import global_db
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError,ParseError

PRODUCT = global_db.get_db('products')

@api_view(['GET'])
def get_all(self):
    return Response(json.dumps(PRODUCT))

@api_view(['GET'])    
def get_by_product_name(self,search_name):
    result = []
    for key,value in PRODUCT.items():
         print(value['product_name'],type(value['product_name']))
         print(search_name,type(search_name))
         if search_name in value['product_name']:
            result.append((key,value))
        
    if not result :
        raise ValidationError("No data. Please refill again.")
    else :              
        return Response(result)

@api_view(['GET'])    
def get_by_id(self,id):
    result = []
    for key,value in PRODUCT.items():
        # print(key,type(key))
        # print(id,type(id))
        if  id == int(key):
            result.append((key,value))
    
    if not result :
        raise ValidationError("No data. Please refill again.")
    else :              
        return Response(result)
        
    