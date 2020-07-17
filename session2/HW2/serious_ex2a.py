# i. 1 and 0 consecutively
# for i in range(1,21):
#     if i % 2 == 1:
#         print(1, end = ' ')
#     else:
#         print(0, end = ' ')  

# ii. Ask users to enter a number n, then print n 1 and 0 in total consecutively:
n = int(input('Enter the total number of 1 and 0: '))
for i in range(1,n+1):
    if i % 2 == 1:
        print(1, end = ' ')
    else:
        print(0, end = ' ')   
