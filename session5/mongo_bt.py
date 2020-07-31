import pyexcel

from pymongo import MongoClient

connection = MongoClient()

quiz_database = connection.get_database('quiz')

result_collection = quiz_database.get_collection('result')

quizzes_collection = quiz_database.get_collection('quizzes')

quizzes_collection.find()

print(list(quizzes))

quizzes = pyexcel.iget_records(file_name='quizzes.xlsx')

right_choices_count = 0

quizzes = list(quizzes)
for quiz in quizzes:
  quiz['choices'] = quiz['choices'].split(',')

  print(quiz['question'])
  for i in range(len(quiz['choices'])):
    print(f' {i+1}. {quiz["choices"][i]} ')

  your_choice = int(input('your choice: ')) - 1
  if your_choice == int(quiz['right_choice']):
    right_choices_count = right_choices_count + 1
  else:
    print('sai mất r :((')

correct_percent = right_choices_count / len(quizzes) * 100
data = [
  ['Đức', f'{correct_percent}%'],
]

data = {
    'name': 'Duc',
    'correct_percent': correct_percent
}

result_collection.insert_one(data)