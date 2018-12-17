import turtle

sides = int(input("How many sides will your shape have? "))

angle = 360 / sides
length = 400 / sides
turtle.fillcolor("blue")
turtle.begin_fill()
for side in range(sides):
    turtle.forward(length)
    turtle.right(angle)

turtle.end_fill()
turtle.done()