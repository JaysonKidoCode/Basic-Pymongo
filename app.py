import pymongo
from pymongo import mongoClient

cluster = MongoClient{"mongodb://Admin:<password>@cluster0-shard-00-00.mbnrh.mongodb.net:27017,cluster0-shard-00-01.mbnrh.mongodb.net:27017,cluster0-shard-00-02.mbnrh.mongodb.net:27017/?ssl=true&replicaSet=atlas-n22dih-shard-0&authSource=admin&retryWrites=true&w=majority"}
db = cluster["test"]
collection = db["test"]

post1 = {"id":5, "name":"Joe"}
post2 = {"id":6, "name":"Bill"}

results = collection.update one({"id":5}, {"$set":{"hello": "5"}})

post count = collection.count documents({})
print(post count)