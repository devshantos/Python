import random

number = [1,2,3,4,5,6,7,8,9]
computer_random= random.choice(number)

while True:
    guessing_number = int(input("Enter your guessing number: "))
    if computer_random == guessing_number:
        print("Congratulations, you are get a chicken dinner")
        break
    else:
        print("Your guessing number is wrong, pls try again")
import random
list = [1,2,3,4,5,6,7,8,9,]

computer_number = random.choice(list)
print(computer_number)

while True:
    guessing_number = int(input("Enter your guessing number: "))
    if guessing_number == computer_number:
        print("Congratulation, you winnenr a chicken dinner")
    else:
        print("Your guessign number is wrong, pls try again.")
