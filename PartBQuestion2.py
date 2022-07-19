import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["exam"]
mycol=mydb["student"]

descMark=mycol.find().sort("Lab_mark.External",-1)
for temp in descMark:
    print(temp["Name"])
print()