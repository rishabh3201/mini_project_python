print("Welcome to my computer quiz!")

playing = input("Do you want to Play? ").lower()


if playing != "yes":
    quit()
score = 0

print("Okay! Let's play:")
print("Questions 1:")
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("correct!")
    score+=1
else:
    print("Incorrect!")

print("Questions 2:")
answer = input("What does GPU stand for? ").lower()
if answer == "graphic processing unit":
    print("correct!")
    score+=1
else:
    print("Incorrect!")


print("Questions 3:")
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("correct!")
    score+=1
else:
    print("Incorrect!")


print("you got " + str(score) + " questions correct!")
print("you got "+ str((score/3)*100)+ "%")
print(f"your total score: {score}/3")