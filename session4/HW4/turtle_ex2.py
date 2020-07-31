from turtle import *
speed(-1)
shape('turtle')
color('blue')

size = 0
for i in range(50):
    for i in range(4):
          forward(size)
          left(90)
          size=size + 1
    left(10)

mainloop()