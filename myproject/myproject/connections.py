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
    
    def get_storage(self,folder_name):
        return self.storage.child(folder_name).get()
    
    def add_storage(self,folder_name,path):
        self.storage.child(folder_name).child(path).put(path)
    
global_db = Database()