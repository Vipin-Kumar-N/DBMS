import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["exam"]
mycol=mydb["student"]

deleteId=mycol.delete_many({"Lab_mark.Internal":{"$lte":30}})
print(deleteId.deleted_count," Deleted Records with Internal Marks <=30 ")
print()
