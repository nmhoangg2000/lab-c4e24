from turtle import *
from turtle3 import draw_square

shape("turtle")
speed(0)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()