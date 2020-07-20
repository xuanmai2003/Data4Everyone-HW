from turtle import *
speed(-1)

for edge in range(3, 8):
    for pencolor in ['red', 'blue', 'brown', 'yellow', 'gray']:
        color(pencolor)
        for pencolor in range(edge): 
            forward(100)
            left(360/edge)
mainloop()