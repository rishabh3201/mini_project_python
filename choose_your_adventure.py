name = input("Type your name: ")
print(f"Welcome {name} to this adventure")
answer = input("You are on dirt road where you want to go! type left/right").lower()


if answer == "left":
    answer = input("walk/swim")
    if answer == "swim":
        print("alligator")
    elif answer == "walk":
        print("no water, you lost")
    else:
        print("not a valid answer! you loose")
elif answer == "right":
    answer = input("cross/back")
    if answer == "cross":
        print("you win")
    elif answer == "back":
        print("back to main road and loose")
    else:
        print("not a valid answer! you loose")
else:
    print("not a valid answer! you loose")



