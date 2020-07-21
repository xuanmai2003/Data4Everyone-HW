print('hc', 'ng', 'ns', 'lm')
words = {
    'hc': 'hoc',
    'ng': 'nguoi',
    'ns': 'noi',
    'lm': 'lam',
}

while True:
    a = input('your code?')
    if a in words:
        print('it means: ', words[a])
    else:
        b = input('not found yor code. do you want to contribute? (Y/N)')
        if b == 'Y' or b == 'y':
            c = input('enter your trans:')
            words[a] = c
            print('updated')
        else:
            break

# teencode_dict = {
#     'nc': 'noi chuyen',
#     'ck': 'chuyen khoan',
#     'vk': 'vu khi',
# }

# while True:
#     print('*'*25)
#     for key in teencode_dict:
#         print(key, end = '\t')
#     print()
#     input_key = input('your code?')
#     if input_key in teencode_dict:
#         print(f'it means:{teencode_dict[input_key]}')
#     else:
#         action = input('not found, do you want to contribute? (y/n)')
#         if action.upper == 'Y':
#             teencode_dict[input_key] = input('Translation: ')
#             print(teencode_dict)
#         else:
#             break

