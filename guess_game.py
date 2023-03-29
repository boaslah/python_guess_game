import random


print("Hello, Welcome to bboaslah's Guess Game.\nGuess a random number between 0 - 100\nand I'll let you know if your guess was wrong or correct");
random = random.randint(0, 100);
user_input = int(input("Please enter your guess: "));

if(user_input == random):
    print("Congratulations! Your guess was right!");
else:
    print("Your guess was wrong.", random, "is the random is the random number." );
