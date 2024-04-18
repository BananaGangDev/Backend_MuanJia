from myproject.connections import global_db
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError,ParseError
import pyrebase
from rest_framework.response import Response
from products import views
import json
from rest_framework import status
<<<<<<< HEAD
# Create your views here.


def create_payment(order_id,amount,slip):
    payment_id = 1 + int(max(list(global_db.get_db('payment').keys())))
=======

# Create your views here.


def create_payment(order_id,amount,slip_url):
>>>>>>> spy-dev
    item = {
        "order_id" : order_id,
        "status" : False,
        "amount" : amount,
<<<<<<< HEAD
        "slip" : slip
    }
    global_db.add_db(db_name='payment',id=payment_id,json=item)
    return payment_id
=======
        "slip" : slip_url
    }
    return global_db.add_db_auto_id(collection='payment',json=item)
>>>>>>> spy-dev

@api_view(['GET'])
def get_payment_by_id(requests,id):
    if requests.method() == 'get':
        result = []
        for key,value in global_db.get_db('order_item').items():
            if  id == int(key):
                result.append((key,value))
        
        if not result :
            return Response("No data. Please refill again.",status=status.HTTP_204_NO_CONTENT)
        else :              
            return Response(result,status=status.HTTP_200_OK)
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST)        
    
@api_view(['PUT'])
def update_status(requests,id,slip):
    if requests.method() == 'put':
        path = slip
        json = {
            "status" : True,
            "slip" : path
        }
        global_db.update_db('payment',str(id),json)
        return Response("Updated Successfully",status=status.HTTP_200_OK)
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST)   
        
    
    
@api_view(['GET'])
def get_payment_by_order_id(requests,id):
    if requests.method() == 'get':
        result = []
        for key,value in global_db.get_db('order_items').items():
            if  id == int(value["order_id"]):
                result.append((key,value))
        
        if not result :
            return Response("No data. Please refill again.",status=status.HTTP_204_NO_CONTENT)
        else :              
            return Response(result,status=status.HTTP_200_OK)    
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)  