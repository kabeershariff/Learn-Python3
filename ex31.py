#Making Decisions

print("""You enter a dark room, You have 2 doors.
      Do you go through door #1 or door #2 ?""")

door = input("> ")

if door == "1":
    print("There is a Giant Snake in here eating something")
    print("What do you do?")
    print("1.Kill Him")
    print("2.Kick It")

    snake = input("> ")
    if snake == "1":
        print("The snake strangles you to death.")
    elif snake == "2":
        print("The snake bites your leg , Game Over")
    else:
        print(f"Well {snake} seems logical")
        print("The snake runs away")

elif door == "2":
    print("You are experiencing something unusual.")
    print("1. Boom Boom Go Postal")
    print("2. Scream")
    print("3. Take a deep breath")

    insanity = input("> ")

    if insanity == "2" or insanity == "3":
        print("You end up dead")

    elif insanity == "1":
        print("Its pretty fun")
    else:
        print("Wrong decisions take lives")

else:
    print("You Die from starvation")
