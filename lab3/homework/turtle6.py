from turtle import *
from random import randint
from turtle5 import draw_star

shape("turtle")
speed(0)
color("blue")
for i in range(100):
    x = randint(-300, 300)
    y = randint(-300, 300)
    length = randint(3,10)
    draw_star(x, y, length)

mainloop()