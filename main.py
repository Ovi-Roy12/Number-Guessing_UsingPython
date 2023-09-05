import random

correct_answer = random.randrange(1,50)
chances =  5

while chances > 0:
    userInput = int(input("Guess the number: "))
    
    if userInput > correct_answer:
        print("The number is too High")
    elif userInput < correct_answer:
        print("The number is too Low")
    else:
        print("Yes!! Match with the number. YOU WIN.")
        break  # Exit the loop if the guess is correct
    
    chances -= 1
    print(f"Chances left: {chances}")

    
print("****************")

if chances == 0:
    print(f"Sorry!! you'v run out of chances.\n"
          f"The correct number is: {correct_answer}\n"
          f"YOU LOSE (*_*)")