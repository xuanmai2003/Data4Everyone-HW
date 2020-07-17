
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))

# delta = (b**2) - (4*a*c)

# if delta < 0:
#     print('vo nghiem')
# elif delta == 0:
#     print('x1 = x2 =', -b / 2*a)
# elif delta > 0:
#     print('x1 =', )

from math import sqrt
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

delta = (b**2) - (4*a*c)

if delta < 0:
    print('vo nghiem')
elif delta == 0:
    x = -b / (2*a)
    print(f'phuong trinh co nghiem kep: {x}')
else:
    x1 = (-b + delta**(1/2))/ (2*a)
    x2 = (-b + sqrt(delta))/ (2*a)
    print(f'phuong trinh co 2 nghiem: {x1, x2}')
