from flask import *

foods = [{'name':'hummos','cal':560 , 'price':35 },
         {'name':'sushi','cal':160 , 'price':45 },
         {'name':'pizza','cal':1160 , 'price':95 },
         {'name':'T-bone','cal':250 , 'price':150 }]

drinks= [{'name':'cola','cal':93 , 'price':7 },
         {'name':'beer','cal':260 , 'price':25 },
         {'name':'sprite','cal':160 , 'price':9 },
         {'name':'gin tonic','cal':150 , 'price':150 }]

app = Flask(__name__)

# foods - get all get by id  post put delete
# drinks - get all get by id post put delete

@app.get('/foods')
def get_all():
    return foods
@app.get('/foods/<int:id>')
def get_by_id(id):
    return foods[id-1]
@app.post('/foods')
def add_food():
    f1 = request.get_json()
    foods.append(f1)
    return 'done',201

@app.delete('/foods/<int:id>')
def delete_food(id):
    foods.pop(id-1)
    return 'done',200

@app.get('/drinks')
def get_all_drinks():
    return foods
@app.get('/drinks/<int:id>')
def get_by_id_drinks(id):
    return foods[id-1]
@app.post('/drinks')
def add_drinks():
    f1 = request.get_json()
    drinks.append(f1)
    return 'done',201

@app.delete('/drinks/<int:id>')
def delete_drinks(id):
    drinks.pop(id-1)
    return 'done',200

app.run()