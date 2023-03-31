import random

counter = 5


print("Hello, Welcome to bboaslah's Guess Game.\nGuess a random number between 0 - 100\nand I'll let you know if your guess was wrong or correct")
random = random.randint(0, 100)

while(counter > 0):
    user_input = int(input("Please enter your guess: "))
    if(user_input == random):
        print("Congratulations! Your guess was right!")
        break
    elif(user_input > random):
        print("Your guess is too high")
    elif(user_input < random):
        print("Your guess is too low", random);
    counter = counter -1
