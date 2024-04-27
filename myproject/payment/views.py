from myproject.connections import global_db
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError,ParseError
import pyrebase
from rest_framework.response import Response
from products import views
import json
from rest_framework import status

# Create your views here.

def create_payment(order_id,amount,slip_url):
    item = {
        "order_id" : order_id,
        "status" : False,
        "amount" : amount,
        "slip" : slip_url
    }
    return global_db.add_db_auto_id(collection='payment',json=item)

@api_view(['GET'])
def get_payment_by_id(request,id):
    if request.method == 'GET':
        payment = global_db.get_db('payment').document(id).get()
        result = []
        if payment :
            payment_id = payment.id
            payment_item = payment.to_dict()
            result.append({payment_id:payment_item})
            return Response(result,status=status.HTTP_200_OK)   
        else :
            return Response(data="No data. Please refill again.",status=status.HTTP_204_NO_CONTENT)
        # result = []
        # for key,value in global_db.get_db('order_item').items():
        #     if  id == int(key):
        #         result.append((key,value))
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST)        
    
@api_view(['PUT'])
def update_status(request,id,slip):
    if request.method == 'PUT':
        path = slip
        url = global_db.add_storage(folder="payment_slip",filename=str(id)+"_slip",path_data=path)
        json = {
            "status" : True,
            "slip" : url
        }
        global_db.update_db('payment',str(id),json)
        return Response("Updated Successfully",status=status.HTTP_200_OK)
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST)   
        
    
@api_view(['GET'])
def get_payment_by_order_id(request,order_id):
    if request.method == 'GET':
        result = []
        for payment in global_db.get_db('payment').streams():
            payment_id = payment.id
            payment_item = payment.to_dict()
            if order_id in payment_item['order_id']:
                result.append({payment_id,payment_item})
            
        if not result :
            return Response(data="No data. Please refill again.",status=status.HTTP_204_NO_CONTENT)
        else :              
            return Response(result,status=status.HTTP_200_OK)
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST)