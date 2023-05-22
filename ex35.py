#Branches and Functions

from sys import exit #Used to Exit

def treasury():
    print("There is a lot of money in here. How much you take away?")
    choice = input("> ")
    if "0" in choice or "1" in choice: #if the string has 0 or 1 then it runs
        how_much = int(choice) #convert string to integers
    else:
        dead("Learn to type numbers!")

    if how_much > 500:
        print("You are greedy you win !!")
        exit(0)

    else:
        dead("Too Nice.")

def snake_room():
    print("There is a snake in here.")
    print("The snake seems to be sitting on a big bag of money.")
    print("How are you going to move it?")
    print("Do you 'snatch money' or 'shout'.")

    snake_moved = False     #A False value which becomes True later

    while True:             #Infinite loop , until we exit the loop
        choice = input("> ")

        if choice == "snatch money":
            dead("The snake bites you.")
        elif choice == "shout" and not snake_moved:
            print("The snake has left the bag.")
            print("You can take the money bag now.")
            print("option unlocked 'open door'.")
            snake_moved = True

        elif choice == "shout" and snake_moved:
            dead("The snake gets angry and bites you.")
        elif choice == "open door" and snake_moved:
            treasury()
        else:
            print("Invalid Input")

def dragon_room():
    print("You see the great evil Dragon!")
    print("Its stare is making you go insane.")
    print("Do you 'flee' or 'kill yourself'.")

    choice = input("> ")
    if "flee" in choice: #if the word is in the string provided we continue better than having to put exact answers
        start()
    elif "kill" in choice:
        dead("Atleast it ends...")
    else:
        dragon_room()  #call the same function again

def dead(why):      #Instead of repeating code create a function
    print(why, "GAME OVER") 
    exit(0)

def start():
    print("You are in a dark room. ")
    print("There is a door to your left and one to your right.")
    print("Choose one!")

    choice = input("> ")

    if choice == "left":
        snake_room()
    elif choice == "right":
        dragon_room()
    else:
        dead("YOU STUMBLE TILL ETERNITY")

start() #Starting function 

