import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate(".env/service_keys.json")
firebase = firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://alegria-audi-blog-default-rtdb.asia-southeast1.firebasedatabase.app"
    },
)
print("Database connected successfully")

db = db.reference("blogs")
