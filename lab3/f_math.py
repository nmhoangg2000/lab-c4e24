from random import randint, choice
from calc import evaluate

#genererate equation
x = randint(0, 9) #4
y = randint(0, 9) #5
error = randint(-1, 1)
r = evaluate(x, y, a) + error

a= choice(["+","-","*","/"])

print(f"{x} {a} {y} = {r}")


user_answer = input("(Y/N)? ").upper()
if error == 0:
    if user_answer == "Y":
       print("yay")
    elif user_answer == "N":
        print("wrong")
else:
    if user_answer == "Y":
        print("wrong")
    elif user_answer == "N":
        print("yay")                 