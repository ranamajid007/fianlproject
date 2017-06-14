from pymongo import MongoClient

# creating connections for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData

empCol = db.Employees.find()

print ('\n All data from EmployeeData Database \n')

for emp in empCol:
        print (emp)
