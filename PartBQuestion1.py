import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["exam"]
mycol=mydb["student"]

updateId=mycol.update_many({"_id":4},{"$set" :{"Vaccination_status":"Both Vaccinated"}})
print(updateId.modified_count," Updated Id:4 ")
print()
