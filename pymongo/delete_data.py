from pymongo import MongoClient

# creating connections for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData

db.Employees.delete_many({"id":'001'})
