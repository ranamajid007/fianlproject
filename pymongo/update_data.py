from pymongo import MongoClient

# creating connections for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData

db.Employees.update_one(
        {"id": '001'},
        {
        "$set": {
            "name":'AAA',
            "age":51,
            "country":'Korea'
        }
        }
    )
