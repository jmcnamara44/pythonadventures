import time
shipName = "Nastrama"
captain = "Wallace"
location = "Earth"
password = "Buttercups"

pAttempt = input("Enter the password: ")
while pAttempt != password:
    if len(pAttempt) < 1: break
    print("Incorrect password silly!")
    pAttempt = input("Enter the password: ")

print("Welcome Captain " + captain + ". We are currently on " + location + ".")

