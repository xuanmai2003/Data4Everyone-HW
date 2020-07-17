# i. 10 x 10 1’s and 0’s, consecutively
# for i in range(1,10):
#     for j in range(1,10):
#         if (i+j) % 2 == 1:
#             print(0, end = '\t')
#         else:
#             print(1, end = '\t')
#     print('')

#ii. Ask users to enter a number n then print n x n 1’s and 0’s consecutively
n = int(input('Enter a number: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i+j) % 2 == 1:
            print(0, end = '\t')
        else:
            print(1, end = '\t')
    print('')