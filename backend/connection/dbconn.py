import pymongo
import gridfs

client = pymongo.MongoClient("mongodb://localhost:27017/")
galenoDatabase = client['neural_net_db']
fs = gridfs.GridFS(galenoDatabase)
