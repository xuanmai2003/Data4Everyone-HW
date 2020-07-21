from turtle import *
speed(-1)

pencolor = ['red', 'blue', 'brown', 'yellow', 'gray']
for edge in range(3, 8):
    color(pencolor[edge - 3])
    for i in range(edge):         
        forward(100)
        left(360/edge)
mainloop()