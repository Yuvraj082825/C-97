import random

print("Number Guessing game")
print("Guess a number (between 1 and 10):")
number=random.randint(1,9)

for i in range(1,6):
    guess=int(input("Enter your guess: "))
    if number==guess:
        print("Congratulations you won!!")
        break
    else:
        if guess<number:
            print("the guessed number is lower than the number")
        else:
            print("the guessed number is higher than the number")
        
