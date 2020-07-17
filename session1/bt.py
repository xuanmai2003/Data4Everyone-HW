a = int(input())

from turtle import *
speed(-1)

for i in range(a):
    forward(100)
    left(360/a)

mainloop()