import turtle
t = turtle.Turtle()
s = int(input("Zadej délku strany: "))
for _ in range(4):
  t.forward(s) 
  t.left(90) 
  turtle.done()