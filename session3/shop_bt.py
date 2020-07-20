# item = ['T-shirt', 'Sweater','Hoodie','Jeans']

# for i in range():
#     n = (input('Welcome to our shop. What do you want? (C R U D):'))
    
#     if n == 'R' or n == 'r':
#         print('our items')
#         for cloth in item:
#             print(cloth)
    
#     else:
#         if n == 'D' or n == 'd':
#             a = int(input('position you want to delete'))
#             item.pop(a)
#         elif n == 'C' or n == 'c':
#             b = input('enter new item')
#             item.append(b)
#         else:
#             index = int(input('position you want to change'))
#             new_item = input('enter new item')
#             item[index] = new_item
#         print('our items')
#         for cloth in item:
#             print(cloth)

#     print('To exit our store please type "EXIT"')
items = ['T-shirt', 'Sweater','Hoodie','Jeans']

def list_out_item():
    for i in range(len(items)):
        # print(i, item{i})
        print(f'{i+1},{items[i]}')

while True:
    action = input('Welcomme to our shop, what do you want? (C R U D): -enter "EXIT" to exit')
    action = action.upper()
    if action == 'C':
        new_item = input('Enter new stuff:')
        items.append(new_item)
        list_out_item()
    elif action == 'R':
        list_out_item()
    elif action == 'U':
        index = int(input('Enter position you want to edit:')) - 1
        if index < (len(items)):
            new_value = input('Enter new value')
            items[index] = new_value
            list_out_item()
        else:
            print('item not in the list')
    elif action == 'D':
        remove_value = input('Enter name of the item you want to delete:')
        if remove_value in items:
            items.remove(remove_value)
            list_out_item()
        else:
            print('item not found')
    elif action == EXIT:
        break