# i. 9x 9 numbers (multiplication table)
# for i in range(1,10):
#     for j in range(1,10):
#         print(i * j, end = '\t')
#     print()

# ii. Ask user to enter a number n then print n x n multiplication table pattern:
n = int(input('Enter a number: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i * j, end = '\t ')
    print()