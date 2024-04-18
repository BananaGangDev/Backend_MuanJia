<<<<<<< HEAD
import pyrebase

config = {
    "apiKey": "AIzaSyCUvHUiypUJEEAV0ymXjJYSATsltEf1SHU",
    "authDomain": "cn334-16626.firebaseapp.com",
    "databaseURL": "https://cn334-16626-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "cn334-16626",
    "storageBucket": "cn334-16626.appspot.com",
    "messagingSenderId": "863452705610",
    "appId": "1:863452705610:web:fc93d111dde9c15e1187b3",
}

class Database:
    def __init__(self):
        self.firebase = pyrebase.initialize_app(config)
        self.authe = self.firebase.auth()
        self.database = self.firebase.database()
        self.storage = self.firebase.storage()
    
    def get_db(self,db_name):
        return self.database.child(db_name).get().val()
    
    def add_db(self,db_name,id,json):
        self.database.child(db_name).child(id).set(json)
        
    def update_db(self,db_name,hopper,json):
        self.database.child(db_name).child(hopper).update(json)
=======
import firebase_admin
from firebase_admin import firestore
from firebase_admin import storage
from firebase_admin import credentials

config = {
  "type": "service_account",
  "project_id": "muanjia",
  "private_key_id": "81cde9689c0d301ebb5e1c0bb782e9afa522f601",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC8/1PGaYMJwViK\nQmj+zs+J5hsgJgnccYcgz+ytaz94oNYCV4actCBXnpkhVBlwIs8emc7IUgi07KoJ\nDOa5hGKmMSua++HOOqCq6YTk9/rcq5yoyeYJ0lr0X1yE3VVPIL/6nWLOgoS3Mu0b\nJ+e9gn/BtbAe5dv3lsA+hq0GnzEr8mUausxhpAX6DV/ytNPgU0OZOOOucuHHpQ5k\n5qiVbOMLZ2O71I6U8u6AIkhxIMXQdqTN+iiLzks5VMuxR+3KYL0heNtkqGIqhgQU\nzg+X38yZpFoW3tZLfxEc4rh81QLRDQ4p0MjECDfl1MkGaI1JTJr+aKmzqsHX26W/\n+iArl0yrAgMBAAECggEAJNaHl7bdKbub7GcBXBknbrOBOgTwCx29vvGIKk0rM/H1\nhMNWo5igbTOmmU5xHuBKCqbkHTuQIuO2SMlQ93wMVmRjIXRTEQVwZ5/YnWCQbw6s\nHGIuCmAMBnHH8MXLaP7zLIAc0C+0epjcilx+2Ptkt3cYew1GkL27fvR1KUNCLFRe\n91QUeS1N/xsuiauxqUeelmOFUg8iewFWaAhqikBshFVerBfwgYV3aycMKDw/klHp\nNQ+HoNVE2TP2yDFJEPokdP2seOgF8BT8uYBVUD4hSgUM8ss4mR2PLi3YiFm5QjHa\n2F1odMkYBHIxdNznlPrkyWakTlRs4B0FnkX0X+DX4QKBgQDl97m6KB92nlP//iwS\nU+cRvA4A7RrXYZAcWoOBDI5VxIUViwfKFZtkJVxGca5FYDE4uxIQxqpGBKfxg3uj\nndEKesDno+ANlQxZAg6OJX5VyDC+WM3+LlqfGgKVHlf5CiTuSeux/A2LMJXR1gm5\n7BmIXvYBBzQbsfDoMqRuowXnaQKBgQDSZFDglCV2nq0yfF2Pybi2fkCn4lJg2gA8\nNCz+MoPAhp2gNTyVLA2mzMu2lDirCKGJ6j/RODJLsxNhfZlH7Jtz+zUjHh9KR+Yx\nS82Ej8WESFOGGgJYzvr+yEvIVxu6dR5LMrzzdy8gCAzJHT6NGojaBaB6UfHqUNih\nBzsbRYcE8wKBgQDRbRd7u3xjxu5SjANQsY4WLX9HQqaWDKhz2c42oNuiqfRU2Sc/\n1wuLWSa+lFqTnXVV568dDf8VArp7DDV1nIw5ke7JRQkO9XSoPmJI+0YhEs2pGzCF\nUWt/xu0hJeAR0TYut6zoitU+tAFMdjKnWacq9OftqcS/j/4HR89NXjNLOQKBgQDP\nPHTV4ddNEltzwUC/o2lIiO/S7oFKWTGmG5a+BK/2ciLNbeLw5OXFiTCX9UQkZGoJ\n2S1nPj18hzXt77OOPyeYhLcAkmkr18qMgCg+DQf3lu5+xxvMsoRVdqH/Ap6TeU2P\nsLih8KIAoS1G5IF6p8ppRuWd1x29OklHxEGaSVAHtQKBgQDBYYMnKQQpZwuktdT9\nsvZJq0MuRoSgVa/miUZqpaDSQStrksX0/M2xbFFuAhjbwQQTpO8K4dX/GD0gz9TN\nQ2HeElNkmXSK0tNazTHc7UYjtm7K62i/5kIks0g/z0rrdxG54dTiGBJ2TsQEV87O\nPhX/KS69d61Fv13uheFyXSaAqA==\n-----END PRIVATE KEY-----\n",
  "client_email": "spy-241@muanjia.iam.gserviceaccount.com",
  "client_id": "116373356867446353378",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/spy-241%40muanjia.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


class Database:
    def __init__(self):
        if not firebase_admin._apps:
            cred = credentials.Certificate('/Users/spy/Backend_MuanJia/myproject/myproject/muanjia-81cde9689c0d.json')        
            firebase_admin.initialize_app(cred)
        
        self.db = firestore.client()
        self.payment_folder = storage.bucket('payment_slip')
        self.product_folder = storage.bucket('product_images')
        
    
    def get_db(self,collection):
        return self.db.collection(collection).stream()
    
    def add_db_with_id(self,collection,document,json):
        self.db.collection(collection).document(document).set(json)
    
    def add_db_auto_id(self,collection,json):
        new_data = self.db.collection(collection.add(json))
        return new_data.id
        
    def update_db(self,collection,document,json):
        self.db.collection(collection).document(document).update(json)
>>>>>>> spy-dev
    
    def get_storage(self,folder_name):
        return self.storage.child(folder_name).get()
    
    def add_storage(self,folder_name,path):
        self.storage.child(folder_name).child(path).put(path)
    
global_db = Database()