a = int(input('Number of pair(s) of rabbits initially:'))
# print('Month 0:',a,'pair(s) of rabbits')
b = a*2
# print('Month 1:',b,'pair(s) of rabbits')
count = 0
for i in range(9):
    print('Month',i, ':',a,'pair(s) of rabbits')
    nth = a + b
    a = b
    b = nth
    count = count + 1