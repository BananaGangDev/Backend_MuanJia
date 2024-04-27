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
import IPython
import os

Apikey='7Nnz7YqING7Q3LMriW4O4ph8VTK6I6aH'
HEADERS = {'apikey': 'OlHGq5r3lOTYWxAxXeQTq2yRq2aJqh4O'}
url = 'https://api.aiforthai.in.th/vaja9/synth_audiovisual'
headers = {'Apikey':Apikey,'Content-Type' : 'application/json'}

@api_view(['GET'])
def get_all(request):
    if request.method == 'GET':
        products_db = global_db.get_db('products').stream()
        products = {}
        for product in products_db:
            product_id = str(product.id)
            product_item = product.to_dict()
            for key,value in product_item.items():
                if key == "product_name":
                    product_name = value
                elif key == "description":
                    description = value
                elif key == "price" :
                    price = value
                elif key == "image_url":
                    image_url = value
                elif key == "sound_url":
                    sound_url = value
            
            data = { product_id : {
                "product_name" : product_name,
                "description" : description,
                "price" : price,
                "image_url" : image_url,
                "sound_url" : sound_url
            }}
            products.update(data)
        
        print(products)
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
    # else : 
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    # for key,value in global_db.get_db('products').items():
    #     if  id == int(key):
    #         # print(value['price'],type(value['price']))
    #         return float(value['price'])
    
@api_view(['POST'])
def get_sound(request,id):
    if request.method == 'POST':
        data = global_db.get_db('products').document(str(id)).get().to_dict()
        text = data['product_name'] + " " + data['description'] + " ราคา " + str(data["price"]) + " บาท "
        data = {'input_text':text,'speaker': 0, 'phrase_break':0, 'audiovisual':0}
        response = requests.post(url, json=data, headers=headers)
        resp = requests.get(response.json()['wav_url'],headers={'Apikey':Apikey})
        print(resp)
        if resp.status_code == 200:
            filename = "audio/" + id + ".wav"
            with open(filename, 'wb') as a:
                a.write(resp.content)
            bucket = global_db.add_storage(folder='sound',filename=filename,path_data=filename)
            if bucket:
                global_db.update_db('product',id,{'sound_url': bucket})
                if os.path.exists(filename):
                    os.remove(filename)
                    return Response(bucket,status=status.HTTP_200_OK)
                else:
                    return Response(data="This file doesn't not exits",status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(data="This file cannot upload",status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data=resp.reason,status=status.HTTP_400_BAD_REQUEST)

    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST)
    