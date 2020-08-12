# import pymysql
# from pymongo import MongoClient

# # connect mongo
# mongo_client = MongoClient()
# mongo_database = mongo_client.get_database('movies')
# mongo_collection = mongo_database.get_collection('movies')

# # connect mysql
# client = pymysql.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'Xuanmai2003!',
#     cursorclass = pymysql.cursors.DictCursor
# )

# database = client.cursor()

# create mysql database
# database.execute("CREATE DATABASE movies")

# database.execute('''
#     CREATE TABLE movies.movie(
#         id VARCHAR(255),
#         title VARCHAR(255),
#         writer VARCHAR(255),
#         year VARCHAR(255),
#         PRIMARY KEY(id)
#     )
# ''')

# database.execute('''
#     CREATE TABLE movies.actor(
#         name VARCHAR(255),
#         PRIMARY KEY(name)
#     )
# ''')

# database.execute('''
#     CREATE TABLE movies.movie_actor(
#         movies_id VARCHAR(255),
#         actor_name VARCHAR(255),
#         PRIMARY KEY(movies_id,actor_name)
#     )
# ''')

# # extrac read(mongo)
# query = {
#     'title': {'$ne': None},
#     'writer': {'$ne': None},
#     'year': {'$ne': None},
#     'actors': {'$ne': None}
# }
# mongo_database = mongo_collection.find({})
# for i in range mongo_database:
#     # transform
#     movies_id = str(movie['_id'])
#     database.execute(f'''
#         INSERT INTO 'movies'.movie('id','title','writer','year')
#         VALUES("{movies_id}","{movie['title']}","{movie['writer']}","{movie['year']}")
#     ''')

# client.commit()

# # extract table
# query = ['
#     {
#         '$unwind': '$actors'
#     },
#     {
#         '$group':{
#             '_id':'$actors'
#         }
#     }
# ]

# actor_database = mongo_collection.aggregate(query)

# for actor in actor_database:
#     database.execute(f'''
#         INSERT INTO 'movies'.actor('name')
#         VALUES("{actor['id']}")
#     ''')

# client.commit()

# query = [{
#     {
#         '$movie': '$actors'
#     },
# }]

# movie_actor_database = mongo_collection.aggregate(query)

# for movie_actor in movie_actor_database:
#     movie_actor_id = str(movie_actor{"_id"})
#     database.execute(f'''
#         INSERT INTO 'movies'.movie_actor('movies_id','actor_name')
#         VALUES("{movie_actor_id}","{movie_actor['actors']})
#     ''')

# client.commit()

import pymysql
from pymongo import MongoClient

#Connect Mongo
mongo_client = MongoClient()
mongo_database = mongo_client.get_database('movies')
mongo_collection = mongo_database.get_collection('movies')

#Connect MySql
client = pymysql.connect(
  host="localhost",
  user='root',
  password="Xuanmai2003!",
  cursorclass = pymysql.cursors.DictCursor
)
database = client.cursor()

# #Create Mysql Database
# database.execute("CREATE DATABASE movies")

# #Create Table Mysql

# database.execute('''
#   CREATE TABLE movies.movie(
#     id VARCHAR(255),
#     title VARCHAR(255),
#     writer VARCHAR(255),
#     year VARCHAR(255),
#     PRIMARY KEY(id)
#   )
# ''')

# database.execute('''
#   CREATE TABLE movies.actor(
#     name VARCHAR(255),
#     PRIMARY KEY (name)
#   )
# ''')

# database.execute('''
#   CREATE TABLE movies.movie_actor(
#     movies_id VARCHAR(255),
#     actor_name VARCHAR(255),
#     PRIMARY KEY(movies_id, actor_name)
#   )
# ''')

# # Extract - Read (mongo)
# query = {
#   'title':{'$ne':None},
#   'writer':{'$ne':None},
#   'year':{'$ne':None},
#   'actors': {'$ne':None}
# }
# movies_database = mongo_collection.find(query)
# for movie in movies_database:
# # #Transform
#   movie_id = str(movie['_id'])
# # #Load
#   database.execute(f'''
#     INSERT INTO `movies`.movie(`id`,`title`,`writer`,`year`)
#     VALUES("{movie_id}","{movie['title']}","{movie['writer']}","{movie['year']}")
#   ''')


#Actor table
#Etract
query = [
  {
    '$unwind':'$actors'
  },
  {
    '$group':{
      '_id':'$actors'
    }
  }
]

actors_database = mongo_collection.aggregate(query)

for actor in actors_database:

  database.execute(f'''
     INSERT INTO `movies`.actor(`name`)
     VALUES("{actor['_id']}")
   ''')

#movie_actor
query = [
  {
    '$unwind':'$actors'
  }
]

movie_actor_database = mongo_collection.aggregate(query)

for movie_actor in movie_actor_database:
  movie_actor_id = str(movie_actor["_id"])
  database.execute(f'''
    INSERT INTO `movies`.movie_actor(`movies_id`,`actor_name`)
    VALUES("{movie_actor_id}","{movie_actor['actors']}")
  ''')


client.commit()