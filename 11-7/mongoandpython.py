import pymongo
import json


client = pymongo.MongoClient('mongodb://localhost:27017')

db=client['foodsanddrinks']

food_collection=db['foods']
drinks_collection=db['drinks']

foods = [x for x in food_collection.find({},{'_id':0})]

# for x in  food_collection.find():
#     foods.append(x)
print(json.dumps(foods))
print(foods)
# print(json.loads(foods))