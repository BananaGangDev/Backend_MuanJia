import datetime
from myproject.connections import global_db
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError,ParseError
import pyrebase
from rest_framework.response import Response
from products import views as product_views
import json
from payment import views as payment_views
from rest_framework import status
# import requests

@api_view(['GET'])
def get_all_order(request):
    if request.method == 'GET':
        order_db = global_db.get_db('order').stream()
        orders = {}
        for order in order_db:
            # print(product.id,product.to_dict())
            order_id = str(order.id)
            order_item = order.to_dict()
            orders.update({order_id : order_item})
        # print(products)
        return Response(data=orders,status=status.HTTP_200_OK)
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_order_items(request):
    if request.method == 'GET':
        return Response(global_db.get_db('order_item'),status=status.HTTP_200_OK)
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def get_order_by_id(request,id):
    if request.method == 'GET':
        order = global_db.get_db('order').document(id).get()
        print(order)
        result = []
        if order :
            order_id = order.id
            order_item = order.to_dict()
            result.append({order_id:order_item})
            return Response(result,status=status.HTTP_200_OK)   
        else :
            return Response(data="No data. Please refill again.",status=status.HTTP_204_NO_CONTENT)
        # result = []
        # for key,value in global_db.get_db('order_item').items():
        #     if  id == int(key):
        #         result.append((key,value))
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET'])
def get_order_item_by_id(request,order_id): #get order items by order id
    if request.method == 'GET':
        result = []
        for order_items in global_db.get_db('order_item'):
            ans = order_items.where("order_id",order_id).stream()
            if ans :
                result.append({ans.id:ans.to_dict()})
            
        return Response(result,status=status.HTTP_200_OK)   
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST)  
           
# @api_view(['POST'])
def create_order_items(order_id,product_id,quantity):
    item = {
        "order_id" : order_id,
        "product_id" : product_id,
        "quantity" : int(quantity)
    }
    return global_db.add_db_auto_id(collection='order_item',json=item)

@api_view(['POST'])
def create_order(request,firstname,lastname,phone,email,address,payment_channel,items):
    if request.method == 'POST':
        # print("before",items)
        items_json = json.loads(items)
        # print("after",items_json,type(items_json))
        total = 0
        order = {
            "firsname" : firstname,
            "lastname" : lastname,
            "phone" : phone,
            "email" : email,
            "address" : address,
            "payment_id" : "",
            "total" : "",
            "payment_channel" : payment_channel 
        }
        order_id = global_db.add_db_auto_id(collection='order',json=order)     
        for key,value in items_json.items():
            # print("item",key)
            create_order_items(order_id=order_id,product_id=str(key),quantity=int((value)))
            total += product_views.get_price_by_id(id=key) * int(value)
                    
        payment_id = payment_views.create_payment(order_id,amount=total,slip_url="None",payment_channel=payment_channel)
        json_data = {
            "payment_id" : payment_id,
            "total" : total,
            "datetime" : datetime.datetime.now()
        }
        global_db.update_db("order",order_id,json=json_data)            
        return Response(data={"order_id":order_id},status=status.HTTP_201_CREATED)
    else :
        return Response(status=status.HTTP_400_BAD_REQUEST)
      