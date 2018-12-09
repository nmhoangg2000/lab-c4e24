from pymongo import MongoClient
uri = "mongodb://admin:admin1@ds227654.mlab.com:27654/c4e24-lab1"
client = MongoClient(uri)
db = client.get_database()
post_collection = db["accounts"]
accounts = [
    {
    "username": "taoooonguuu",
    "email":"nmhoangxxi2000@gmail.com",
    "phone":"0123456789",
    "password":"hoang2510",
    "yob":"2000"
    },
    {
    "username": "taooonguuu",
    "email":"nmhoanxxi2000@gmail.com",
    "phone":"012356789",
    "password":"hoang2510",
    "yob":"2001"
    },
    {
    "username": "taoooonuuu",
    "email":"nmhoangxi2000@gmail.com",
    "phone":"012345789",
    "password":"hoang2510",
    "yob":"2001"
    }
]

for i in range (len(accounts)):
       
post_collection.insert_one(accounts)
client.close()