#use input() function for Python 3
name = input("Enter your name: ")

#random number guessing game
from numpy import random

# display a greeting by calling the name and a welcome to the game
print('Hello, ' + name +'!' + ' Welcome to the guessing game!!!')
print("----------")

# The guessing number should be between 1 and 10.
actual_number = random.randint(1,10)

# Guess the attempt of the number of guess
number_of_guesses = 0

# While Loops, as long the number_of_guesses is inferior to 5 attempts; the number is an integer. 
# Keep the loop going as long the number_of_guess is not equal to five attempts.
while number_of_guesses < 5:
#prompt user to enter a number
    guess = int(input("Guess the number:\n"))
# increment number_of_guess by 1
    number_of_guesses += 1

# Display too low as long the guessing number is lesser than the actual number
    if guess < actual_number:
        print("Your guess was too low")
# Display too high as long the guessing number is higher than the actual number
    elif guess > actual_number:
        print("Your guess was too high")
# End game if the condition is met.
    if guess == actual_number:
        print(f"\nCorrect, you guessed the number in {number_of_guesses} attempts.")
        break
    
# if none of these conditions are true, end the game.
else:
    print('\nOops invalid guess try again, the actual number is ' + str(actual_number)+'.')

#spacing
print("\n----------")
print('Thank you for playing!')
#spacing
print("----------")
