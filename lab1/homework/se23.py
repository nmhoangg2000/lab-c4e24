from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
post_collection = db["post"]
new_document ={
    "title":"???",
    "authur": "HOÀNG",
    "content":"J'amie la salle de classe"
}
post_collection.insert_one(new_document)
client.close()