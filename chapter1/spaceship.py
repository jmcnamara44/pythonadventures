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

choice = ""
while choice != "/exit":
    print("What would you like to do?")
    print("a: Travel to another planet")
    print("b: Fire the cannons")
    print("c: Open the airlock")
    print("d: Self-destruct")
    print("/exit to exit")
    choice = input("Enter choice here: ")
    
    if choice == "a":
        destination = input("Where would you like to go? ")
        print("Leaving " + location + " and entering " + destination)
        time.sleep(5)
        print("arrived at {0}".format(destination))
        location = destination
    elif choice == "b":
        print("Firing cannons")
        time.sleep(1)
        print("BANG!")
        time.sleep(1)
    elif choice == "c":
        print("Opening airlock")
        time.sleep(2)
        print("Airlock open")
        time.sleep(1)
    elif choice == "d":
        confirm = input("Are you sure you want to destory the ship? (y/n)")
        
        if confirm == "y":
            print("Ship will self-destruct in 3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("Goodbye")
            print("BOOM!")
            choice = "/exit"
    elif choice == "/exit":
        print("Goodbye")
    else:
        print("Selection is not valid, try again")