from matplotlib import pyplot
from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
customers_collection = db["customers"]
count_events = 0
count_ads = 0
count_wom = 0
for i in customers_collection.find():
    if i["ref"].count("events") == 1:
        count_events += 1
    elif i["ref"].count("ads") == 1:
        count_ads += 1
    elif i["ref"].count("wom") == 1:
        count_wom += 1

customers_ref_counts = [count_events, count_ads, count_wom]
customers_ref_names = ["events", "ads", "wom"]
print(customers_ref_names, customers_ref_counts)

pyplot.pie(customers_ref_counts, labels=customers_ref_names, autopct="%.0f%%", shadow=True, explode=[0, 0.1, 0])
pyplot.title("References")
pyplot.axis("equal")

pyplot.show()

client.close()