from pymongo import MongoClient

# creating connections for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData

db.Employees.insert_one(
        {
        "id": '001',
            "name":'ABC',
        "age":50,
        "country":'Korea'
        })

db.Employees.insert_many([
{
         "id": '002',
             "name":'DEF',
         "age":51,
         "country":'China'
         },
{
         "id": '003',
             "name":'GHU',
         "age":41,
         "country":'Japan'
         }
]
)