from calc import evaluate

x = int(input("x = "))
y = int(input("y = "))
pt = input("pt: ")

r = evaluate(x, y, pt)

# if pt == "+":
#     r= x + y
# elif pt == "-":
#     r = x -y
# elif pt =="*":
#     r=x*y    
# elif pt == "/":
#     r=x/y

print(r)    
