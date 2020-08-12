from pymongo import MongoClient
from bson import ObjectId
connection = MongoClient()
movies_database = connection.get_database('mongo_ex')
# movies_collection = movies_database.get_collection('movies')

# movies_found = movies_collection.find({'writer': 'Quentin Tarantino'})
# print(list(movies_found))

# movies_found = movies_collection.find({'actors': 'Brad Pitt'})
# print(list(movies_found))

# movies_found = movies_collection.find({'franchise': 'The Hobbit'})
# print(list(movies_found))

# movies_found = movies_collection.find({'year': {'$lt':2000}})
# print(list(movies_found))

# movies_found = movies_collection.find({
#     'year': {'$lt':2000 },
#     'year': {'$gt': 2010}
#     })
# print(list(movies_found))

# movies_found = movies_collection.find({'title': 'The Hobbit: An Unexpected Journey'})
# print(list(movies_found))
# movies_collection.update_one(
#     {'title': 'The Hobbit: An Unexpected Journey'},
#     {
#         '$set': {'synopsis':'A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug.'}
#     }
# )

# movies_found = movies_collection.find({'title': 'The Hobbit: The Desolation of Smaug'})
# print(list(movies_found))
# movies_collection.update_one(
#     {'title': 'The Hobbit: The Desolation of Smaug'},
#     {
#         '$set': {'synopsis':'The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring.'}
#     }
# )

# movies_found = movies_collection.find({'title': 'Pulp Fiction'})
# print(list(movies_found))
# movies_collection.update_one(
#     {'title': 'Pulp Fiction'},
#     {
#         '$push': {'actors':'Samuel L. Jackson'}
#     }
# )

# movies_found = movies_collection.find({'synopsis': {'$regex':'Bilbo'}})
# print(list(movies_found))

# movies_found = movies_collection.find({'synopsis': {'$regex': 'Gandalf'}})
# print(list(movies_found))

# movies_found = movies_collection.find({
#     'synopsis': {'$regex':'Bilbo'},
#     'synopsis': {'$ne':{'regex': 'Gandalf'}}
#     })
# print(list(movies_found))

# movies_found = movies_collection.find({
#     'synopsis': {'$regex':'dwarves'} or 'synopsis': {'$regex': 'hobbit'}
#     })
# print(list(movies_found))

# movies_found = movies_collection.find({
#     'synopsis': {'$regex':'gold'},
#     'synopsis': {'$regex':'dragon'}
#     })
# print(list(movies_found))

# movies_collection.delete_many({'title':"Pee Wee Herman's Big Adventure"})

# movies_collection.delete_many({'title':"Avatar"})

# users_collection = movies_database.get_collection('users')
# users_found = users_collection.find()
# print(list(users_found))

# posts_collection = movies_database.get_collection('posts')
# posts_found = posts_collection.find()
# print(list(posts_found))

# posts_collection = movies_database.get_collection('posts')
# posts_found = posts_collection.find({'username':'GoodGuyGreg'})
# print(list(posts_found))

# posts_collection = movies_database.get_collection('posts')
# posts_found = posts_collection.find({'username':'ScumbagSteve'})
# print(list(posts_found))

# comments_collection = movies_database.get_collection('comments')
# comments_found = comments_collection.find()
# print(list(comments_found))

# comments_found = comments_collection.find({'username':'GoodGuyGreg'})
# print(list(comments_found))

# comments_found = comments_collection.find({'username':'ScumbagSteve'})
# print(list(comments_found))

# comments_found = comments_collection.find({'post': ObjectId('5ed8ed2b0c5696489b1631f6')})
# print(list(comments_found))