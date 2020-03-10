from pymongo import MongoClient
client = MongoClient()

db = client.test

cshr = db.CarSeatHeadrest
data = {
    'Learned to turn the light off': {
        'rating': 0.12,
        'song': 'Dont Remind me',
    }
}
cshr.insert_one(data)

for member in cshr.find():
    print(member)

