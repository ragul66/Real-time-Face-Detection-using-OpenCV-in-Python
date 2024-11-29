import firebase_admin
from firebase_admin import credentials

cred=credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognitionrealtime-3c939-default-rtdb.firebaseio.com/"
})
