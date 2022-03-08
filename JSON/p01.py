import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

car = Vehicle('Tata Nexon','1499cc',739000)

car_json = json.dumps(car.__dict__)

print('Type of JSON file converted: ',type(car_json))

with open("vehicles.json", "w") as v:
    json.dump(car.__dict__, v)

print("Object of class Vehicle:", car.__dict__, type(car.__dict__))

with open("vehicles.json", "r") as car_data:
    car_data = json.load(car_data)

print("JSON to Python:", car_data, type(car_data))
