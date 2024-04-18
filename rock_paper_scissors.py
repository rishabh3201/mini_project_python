import random

user_wins = 0
computer_wins = 0
draw = 0
options = ["rock", "paper", "scissors"]
while True:
    user_input = input("type Rock/Paper/Scissors or Q to quit ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue
    random_number = random.randint(0,2)
    # rock: 0 paper:1 scissors: 2
    computer_pick = options[random_number]
    print(f"computer Picked: {computer_pick}.")
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins+=1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins+=1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins+=1
    
    elif user_input == computer_pick:
        print("draw")
        draw+=1
    else:
        print("you lost!")
        computer_wins+=1

print(f"You won {user_wins}.")
print(f"Computer won {computer_wins}.")
print(f"Draw: {draw}.")
print(f"Total Matches: {user_wins + computer_wins + draw}")
print("GoodBye!")