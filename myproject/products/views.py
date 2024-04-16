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

PRODUCT = global_db.get_db('products')

@api_view(['GET'])
def get_all(self):
    if requests.method() == 'get':
        return Response(data=json.dumps(PRODUCT),status=status.HTTP_200_OK)
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])    
def get_by_product_name(requests,search_name):
    if requests.method() == 'get':
        result = []
        for key,value in PRODUCT.items():
            print(value['product_name'],type(value['product_name']))
            print(search_name,type(search_name))
            if search_name in value['product_name']:
                result.append((key,value))
            
        if not result :
            return Response(data="No data. Please refill again.",status=status.HTTP_204_NO_CONTENT)
        else :              
            return Response(result,status=status.HTTP_200_OK)
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])    
def get_product_by_id(requests,id):
    # print(id,type(id))
    if requests.method() == 'get':
        result = []
        for key,value in PRODUCT.items():
            if  id == int(key):
                result.append((key,value))
        
        if not result :
            return Response(data="No data. Please refill again.",status=status.HTTP_204_NO_CONTENT)
        else :              
            return Response(result,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
def get_price_by_id(id):
    for key,value in PRODUCT.items():
        if  id == int(key):
            # print(value['price'],type(value['price']))
            return float(value['price'])
    
