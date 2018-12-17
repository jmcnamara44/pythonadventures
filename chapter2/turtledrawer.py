import turtle

length = 20
angle = 45
movecounter = 0
while movecounter < 4:
    turtle.forward(length)
    turtle.right(angle)
    turtle.forward(length)
    turtle.left(angle)
    movecounter +=1
    
input("are you done")

