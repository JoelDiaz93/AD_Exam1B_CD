from TikTokApi import TikTokApi
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

api = TikTokApi()
results = 10
trending = api.trending(count=results)

CLIENT = MongoClient("mongodb://localhost:27017/")
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)
db = CLIENT["python"]
tiktok = db["tiktok"]

x = tiktok.insert_many(trending)

print(trending)
print(type(trending))