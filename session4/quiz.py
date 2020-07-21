import pyexcel

quizzes = pyexcel.iget_records(file_name = 'quiz.xlsx')
for quiz in quizzes:
    quiz['choice'] = quiz['choice'].split(',')
# quizzes = [
# {
#     'question': 'con nhen co may chan?',
# 'choices': [3,4,5,6],
# 'right_choice': 3
# },
# {
#     'question': 'con cho co may chan?',
# 'choices': [3,4,5,6],
# 'right_choice': 1
# }
# ]

# right_choice_count = 0
# for quiz in quizzes:
#     print(quiz['question'])
#     for i in range(len(quiz['choices'])):
#         print(f'{i+1},{quiz["choices"][i]}')

#     a = int(input('your answer:'))
#     if a == quiz['right_choice'] + 1:
#         print('correct')
#         score = right_choice_count + 1
#     else:
#         print('incorrect')

# percentage = score / len(quizzes) * 100
# print(f'{percentage}%')      

right_choices_count = 0

for quiz in quizzes:
  print(quiz['question'])
  for i in range(len(quiz['choices'])):
    print(f' {i+1}. {quiz["choices"][i]} ')

  your_choice = int(input('your choice: ')) - 1
  if your_choice == quiz['right_choice']:
    right_choices_count = right_choices_count + 1
  else:
    print('sai mất r :((')

correct_percent = right_choices_count / len(quizzes) * 100
print(f'{correct_percent}%')
# # data = [
# # ['Duc',correct_percent]
# # ]
# # pyexcel.save_as(array=data, dest_file_name='quiz.xlsx')
# data = [
#   ['Đức', f'{correct_percent}%'],
# ]
# pyexcel.save_as(array=data, dest_file_name='quiz.xlsx')
