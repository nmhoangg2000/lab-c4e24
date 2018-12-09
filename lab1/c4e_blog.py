from pymongo import MongoClient


#1 connect to database server
uri = "mongodb://admin:admin1@ds227654.mlab.com:27654/c4e24-lab1"
client = MongoClient(uri)
#2 select database
db = client.get_database()

#3 select collection
post_collection = db["posts"]
for post in post_collection.find():
    print(post)

#4 create document
# new_document = {
#     "title": "hôm nay trời nắng",
#     "post": "mình vẫn ở nhà ... láo, tao đi bão",
# }
# #5 add document into collection
# post_collection.insert_one(new_document)
# #6 close connection
# client.close()