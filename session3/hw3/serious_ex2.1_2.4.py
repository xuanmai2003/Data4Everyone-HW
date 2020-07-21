print('Hello, my name is Mai adn these are the sizes of my sheeps:')
sheep_size = [5,7,300,90,24,50,75]
print(sheep_size)

a = int(max(sheep_size))
print('Now my biggest sheep has size', a, 'lets shear it')
b = sheep_size.index(a)
sheep_size[b] = (8)
print('After shearing, here is my flock')
print(sheep_size)

new_sheep_size = []
for i in sheep_size:
    new_sheep_size.append(i + 50)
print('One month has passed, now here is my flock')
print(new_sheep_size)

# c = int(max(new_sheep_size))
# print('Now my biggest sheep has size', c, 'lets shear it')
# d = new_sheep_size.index(c)
# new_sheep_size[d] = (8)
# print('After shearing, here is my flock')
# print(new_sheep_size)


