#Prompt qn input in Python3 to call the name
name = input("Enter your name: ")

# Import the module moduleGreeting, and call the greeting function
import moduleGreeting
moduleGreeting.greeting(name)

#spacing
print("----------")

# Guess the number
actual_number = 55
number_of_guesses = 0

# While True Loops, we declare the number_of_guesses and the guess to be integer. 
# Keep going as long the number_of_guess is not equal to actual_number (55)
while True:
    # increment number_of_guess by 1
    number_of_guesses += 1
    guess = int(input("Guess the number:"))
    if guess < actual_number:
        print("Your guess was too low")

    elif guess > actual_number:
        print("Your gues was too high")
    
    # if none of these conditions are true
    else:
        print(f"Correct, you guessed the number in {number_of_guesses} attempts.")
        break
#spacing
print("----------")
print('Thank you for playing!')
#spacing
print("----------")
