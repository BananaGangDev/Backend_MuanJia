import datetime
from myproject.connections import global_db
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError,ParseError
import pyrebase
from rest_framework.response import Response
from products import views
import json
from rest_framework import status
from rest_framework.parsers import (MultiPartParser, FormParser)
import os
import base64
from django.core.files.base import ContentFile
# Create your views here.

def create_payment(order_id,amount,slip_url):
    item = {
        "order_id" : order_id,
        "status" : False,
        "amount" : amount,
        "slip" : slip_url,
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
def update_status(request,id,image):
    if request.method == 'PUT':
        payment_id = get_payment_by_order_id(id)
        if payment_id == "":
            return Response(data="No Data,Please Refill Again",status=status.HTTP_204_NO_CONTENT)
        
        path_slip = upload_image(payment_id,image=image)
        datatype = path_slip.split('.')[-1]
        with open(path_slip, 'wb') as a:
            url = global_db.add_storage(folder='payment_slip',filename=payment_id+"."+datatype,path_data=path_slip)
            if url:
                global_db.update_db('payment',str(payment_id),{'slip': url})
                global_db.update_db('payment',str(payment_id),{'status': True})
                global_db.update_db('payment',str(payment_id),{'paid_datetime': datetime.datetime.now()})
                if os.path.exists(path_slip):
                    os.remove(path_slip)
                    return Response(data=id,status=status.HTTP_200_OK)
                else:
                    return False
            else:
                return False
    else : 
        return Response(status=status.HTTP_400_BAD_REQUEST)   
        
def get_payment_by_order_id(order_id):
    result = []
    for payment in global_db.get_db('payment').stream():
        payment_id = payment.id
        payment_item = payment.to_dict()
        if order_id == payment_item['order_id']:
            return payment_id
            
    return ""

def upload_image(id,image):
    fm,imgstr = image.split(';base64,')
    ext = fm.split('/')[-1]
    filename = id + "." + ext
    path = "image/" + filename
    padding = 4 - len(imgstr) % 4
    if padding:
        imgstr += "=" * padding
    image_data = base64.b64decode(imgstr)
    with open(path, 'wb') as a:
        a.write(image_data)
    return path
    
