from flask import *
import pymongo


client = pymongo.MongoClient('mongodb://localhost:27017')

db=client['foodsanddrinks']

food_collection=db['foods']
drinks_collection=db['drinks']

app = Flask(__name__)

# foods - get all get by id  post put delete
# drinks - get all get by id post put delete

@app.get('/foods')
def get_all():
    foods=[x for x in  food_collection.find()  ]
    print(foods)
# @app.get('/foods/<int:id>')
# def get_by_id(id):
#     return foods[id-1]
# @app.post('/foods')
# def add_food():
#     f1 = request.get_json()
#     foods.append(f1)
#     return 'done',201
#
# @app.delete('/foods/<int:id>')
# def delete_food(id):
#     foods.pop(id-1)
#     return 'done',200
#
# @app.get('/drinks')
# def get_all_drinks():
#     return foods
# @app.get('/drinks/<int:id>')
# def get_by_id_drinks(id):
#     return foods[id-1]
# @app.post('/drinks')
# def add_drinks():
#     f1 = request.get_json()
#     drinks.append(f1)
#     return 'done',201
#
# @app.delete('/drinks/<int:id>')
# def delete_drinks(id):
#     drinks.pop(id-1)
#     return 'done',200

app.run()