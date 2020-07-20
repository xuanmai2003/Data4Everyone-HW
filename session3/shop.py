# stuff1 = 'ao tam'
# stuff2 = 'ao mua'
# stuff3 = 'ao phao'


stuffs = ['ao tam', 'ao mua', 'ao phao','quan boi']
# print(stuffs) #Read
# print(len(stuffs))

# print(stuffs[-1]) #Read one
# ao_mua = stuffs [1]
# print(ao_mua)
# #Read All
# for i in range(len(stuffs)):
#     print(stuffs[i])

# index = int(input('vi tri muon sua'))
# new_item = input('ten item moi')
# stuffs[index] = new_item #Update

stuffs.pop(-1) # delete by index
stuffs.remove('ao phao') # delete by value

# new_item = input('enter new item')
# stuffs.append(new_item) # Create new item
print(len(stuffs))
#Read All 2
for item in stuffs:
    print(item)