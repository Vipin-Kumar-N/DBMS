import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["exam"]
mycol=mydb["student"]

mylist = [
    {"_id":1,"Name":"ANJALI","Place":"KOLLAM","Phone":8582639562,"Vaccination_status":"Both Vaccinated","RTPCR":"negative","Lab_mark":{"Internal":30,"External":45},"Department":"MCA"},
    {"_id":2,"Name":"ANURADHA","Place":"VARKALA","Phone":9992639562,"Vaccination_status":"Both Vaccinated","RTPCR":"negative","Lab_mark":{"Internal":40,"External":48},"Department":"CIVIL"},
    {"_id":3,"Name":"BISMIYA","Place":"KOLLAM","Phone":9446639562,"Vaccination_status":"not Vaccinated","RTPCR":"positive","Lab_mark":{"Internal":50,"External":39},"Department":"MCA"},    
    {"_id":4,"Name":"VIMAL","Place":"ERNAKULAM","Phone":8582639568,"Vaccination_status":"First dose only","RTPCR":"positive","Lab_mark":{"Internal":40,"External":42},"Department":"CIVIL"},
    {"_id":5,"Name":"VIVEK","Place":"KOLLAM","Phone":8582639777,"Vaccination_status":"Both Vaccinated","RTPCR":"negative","Lab_mark":{"Internal":50,"External":50},"Department":"MCA"}
    ]

new=mycol.insert_many(mylist)
print(new.inserted_ids)
