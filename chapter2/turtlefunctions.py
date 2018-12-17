import turtle

def drawShape(sides, length):
    angle = 360 / sides
    for side in range(sides):
        turtle.forward(length)
        turtle.right(angle)
        
def drawSquare(length):
    drawShape(4, length)
    
def drawTriangle(length):
    drawShape(3, length)
    
def drawCircle(length):
    drawShape(360, length)

def moveTurtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
drawSquare(10)
moveTurtle(60, 30)
drawTriangle(20)
moveTurtle(-100, -30)
drawCircle(2)
turtle.done()