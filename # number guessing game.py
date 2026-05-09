# number guessing game 

import random # module used to generate random numbers 

top_of_range = input("type a number: ")

if top_of_range.isdigit(): # checking if the input contains only digits
    top_of_range = int(top_of_range)
    
    if top_of_range <=0:
        print('pls type a number larger than 0 next time')
        quit()
else:
    print('pls type a number next time')   # runs if input is not a valid num
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0 # variable to count no of guesses

while True:
    guesses +=1 # increasing guess count in every round
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print('pls type a num next time.')
        continue
    if user_guess == random_number:
        print("you got it!")
        break
    elif user_guess > random_number:
            print("you were above the number!")
    else:
            print("you were below the number!")
            
       
print("you got it in", guesses, "guesses")
       

    
# logic:
# 1. ask the user to enter the top range for the game
# 2. check if the input is a valid positive number
# 3. generate a random number between 1 and the range
# 4. keep asking the user to guess the number
# 5. tell the user if their guess is too high or too low
# 6. stop the game when they guess correctly
# 7. display total number of guesses taken