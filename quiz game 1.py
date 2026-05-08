# thinking logic for a quiz game

# ask users a bunch of questions and if they give right answer to the ques, add one to their score 
# end of the program print what they got out of num of questions.

print("welcome to the quiz<3") 

playing = input("do you wanna play?") # ask if they wanna play, then # check if the user typed yes 

if playing.lower() != "yes":
    quit() # if no, thenn quit
print("okay, let's play :) ")
score = 0
    
answer = input( "what does CPU stand for? ")
if answer.lower() == "central processing unit": # ans has to match exactly wit what the user typed in 
    print('Correct!') 
    score += 1
else: 
    print("incorrect") # anything other than central processing unit, thee else statement runs
    
answer = input( "what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!') 
    score += 1
else: 
    print("incorrect")
    
answer = input( "what does RAM stand for? ")
if answer.lower() == "random access memory": # ans has to match exactly wit what the user typed in 
    print('Correct!') 
    score += 1
else: 
    print("incorrect")
    
answer = input( "what does PSU stand for? ")
if answer.lower() == "power supply unit": 
    print('Correct!') 
    score += 1
else: 
    print("incorrect")
    
print(" you got " + str(score) + " questions correct")
print(" you got " + str((score/4) * 100) + "%.")