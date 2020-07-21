print('Hello, my name is Mai adn these are the sizes of my sheeps:')
sheep_size = [5,7,300,90,24,50,75]
print(sheep_size)

a = int(max(sheep_size))
print('Now my biggest sheep has size', a, 'lets shear it')
b = sheep_size.index(a)
sheep_size[b] = (8)
print('After shearing, here is my flock')
print(sheep_size)

print('MONTH 1')
sheep_size_month_1 = []
for i in sheep_size:
    sheep_size_month_1.append(i + 50)
print('One month has passed, now here is my flock')
print(sheep_size_month_1)

c = int(max(sheep_size_month_1))
print('Now my biggest sheep has size', c, 'lets shear it')
d = sheep_size_month_1.index(c)
sheep_size_month_1[d] = (8)
print('After shearing, here is my flock')
print(sheep_size_month_1)

print('MONTH 2')
sheep_size_month_2 = []
for i in sheep_size_month_1:
    sheep_size_month_2.append(i + 50)
print('One month has passed, now here is my flock')
print(sheep_size_month_2)

e = int(max(sheep_size_month_2))
print('Now my biggest sheep has size', c, 'lets shear it')
f = sheep_size_month_2.index(e)
sheep_size_month_2[f] = (8)
print('After shearing, here is my flock')
print(sheep_size_month_2)

print('Month 3')
sheep_size_month_3 = []
for i in sheep_size_month_2:
    sheep_size_month_3.append(i + 50)
print('One month has passed, now here is my flock')
print(sheep_size_month_3)

total = int(sum(sheep_size_month_3))
print('My flock has size in total:', total)
print('I would get:', total,'*$2 = $',total*2)
