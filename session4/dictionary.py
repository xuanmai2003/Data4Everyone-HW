person = ['Duc', 96, 175, 70, 'Son La', True, False, 1]

person_dict = {
    'name': 'Duc',
    'yob': 96,
    'height': 175,
    'weight': 70,
    'nam': 0,
}
if 'name' in person_dict: #check if key is in dictionary
    print(person_dict['height']) #Read one

person_dict['job'] = 'dev' # create

person_dict['name'] = 'duc' #update

for key in person_dict:
    print(person_dict[key]) #Read all

del person_dict['nam'] #delete