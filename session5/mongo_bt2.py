import pyexcel

from pymongo import MongoClient

connection = MongoClient()

quiz_database = connection.get_database('quiz')

quizzes_collection = quiz_database.get_collection('quizzes')

records = pyexcel.iget_records(file_name='quizzes.xlsx')

# for record in records:
#     quizzes_collection.insert_one({
#         'questions': record['question'],
#         'choices': record['choices'].split(','),
#         'right_choice': record['right_choice']
#     })

list_data = []
for record in records:
    

