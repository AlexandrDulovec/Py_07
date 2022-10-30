import turtle
t = turtle.Turtle()
s = int(input("Zadej počet stran: "))
d = int(input("Zadej délky stran: "))
for _ in range(s):
    turtle.forward(d)
    turtle.right(360 / s)