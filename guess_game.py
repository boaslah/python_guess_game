import random

counter = 5


print("Hello, Welcome to the ODC Guess Game.\nYou have 5 chances to guess a random number between 0 - 100")
random = random.randint(0, 100)

while(counter):
    user_input = int(input("Please enter your guess: "))
    if(user_input == random):
        print("Congratulations! Your guess was right!")
        break
    elif(counter == 1):
        print("You have reached the end of your chances. The right guess is", random)
        break
    elif(user_input > random):
        print("Your guess is too high")
    elif(user_input < random):
        print("Your guess is too low")
    counter = counter -1
