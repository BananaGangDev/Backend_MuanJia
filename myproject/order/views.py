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
# Create your views here.
#order 1000X
#payment 2000X
#product 3000X
#order_item 4000X

@api_view(['GET'])
def get_all_order(request):
    if request.method == 'GET':
        return Response(global_db.get_db('order'),status=status.HTTP_200_OK)
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def get_all_order_items(request):
    if request.method == 'GET':
        return Response(global_db.get_db('order_items'),status=status.HTTP_200_OK)
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def get_order_by_id(request,id):
    if request.method == 'GET':
        result = []
        for key,value in global_db.get_db('order').items():

            if  id == int(key):
                result.append((key,value))
        
        if not result :
            return Response("No data. Please refill again.",status=status.HTTP_204_NO_CONTENT)
        else :              
            return Response(result)    
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def get_order_item_by_id(request,id):
    if request.method == 'GET':
        result = []
        for key,value in global_db.get_db('order_items').items():
            if  id == int(value['order_id']):
                result.append((key,value))
        
        if not result :
            return Response("No data. Please refill again.",status=status.HTTP_204_NO_CONTENT)
        else :              
            return Response(result)     
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST) 
           
# @api_view(['POST'])
def create_order_items(order_id,product_id,quantity):
    if not global_db.get_db('order_items'):
        item_id = 40000 + 1
    else : 
        item_id = 1 + int(max(list(global_db.get_db('order_items').keys())))
    item = {
        "order_id" : order_id,
        "product_id" : product_id,
        "quantity" : quantity
    }
    global_db.add_db(db_name='order_items',id=item_id,json=item)
    print(item_id)
    

@api_view(['POST'])
def create_order(request,firstname,lastname,phone,email,address,items):
    if request.method == 'POST':
        total = 0
        if not global_db.get_db('order'):
            order_id = 10000 + 1
        else : 
            order_id = 1 + int(max(list(global_db.get_db('order').keys())))
        items_json = json.loads(items)
        for item in items_json:
            create_order_items(order_id=order_id,product_id=str(item),quantity=items_json[item])
            total += product_views.get_price_by_id(int(item)) * items_json[item]
                    
        payment_id = payment_views.create_payment(order_id,amount=total,slip="eiei")            
        order = {
            "firsname" : firstname,
            "lastname" : lastname,
            "phone" : phone,
            "email" : email,
            "address" : address,
            "payment_id" : payment_id,
            "total" : total,
        }        
        global_db.add_db(db_name='order',id=order_id,json=order)
        return Response(data="Created order successfully",status=status.HTTP_201_CREATED)
    else :
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
            
    
    