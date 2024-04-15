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
    
    def get_db(self,db_name):
        return self.database.child(db_name).get().val()
    
global_db = Database()