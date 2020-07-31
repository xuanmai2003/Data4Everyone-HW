from pymongo import MongoClient
from bson import ObjectId

connection = MongoClient() # connect to mongodb

new_database = connection.get_database('D4E15') # create / get database
quiz_database = connection.get_database('quiz')

result_collection = quiz_database.get_collection('result')
new_collection = new_database.get_collection('students') # create / get collection

# new_collection.insert_one({'name': 'first data'}) # write document to collection
result_found = result_collection.find({'name': 'Duc'})
print(list(result_found))

result_collection.update_one(
    {'_id': ObjectId("5f202b00a5936af5354a9b2b")}, #query
    {
        '$set': {'correct_percent': 100} #push, set, unset
    } #update
)

# result_collection.delete_many({'corret_percent':{'$lte': 50}})