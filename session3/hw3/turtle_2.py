from turtle import *
speed(-1)

for colors in ['red', 'blue', 'brown', 'yellow', 'gray']:
    color(colors)
    begin_fill()
    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()    

mainloop()