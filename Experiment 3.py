import random #for calling database that works like a generator

a=0 #lowest number of the guessing game
b=50 #threshold of the guessing game

print ('Guessing Game!') #informs the user that the user will play a guessing game

generated= random.randint (a,b) #for generating a random number that the user will have to guess
print() #new line in the terminal 
print ("You only have 10 chances") #informs the user that only 10 chances will be given to guess the random generated number

#start of loop function
chance = 0 #variable to use to display the user's tries to guess the number
while chance <= 10: #use of while until variable chance reaches 10 loops to stop the loop
    chance +=1
    
    print()
    guess = int(input("Guess a number between 0 & 50: ")) #asks the user what the random generated number is

    if guess == generated:
        print()
        print("Congratulations your answer is correct, you did it in", chance, "try/tries") 
        #when user guessed it right, program will display 
        #how many the user tried to guess the number using the chance variable
        break
        #also breaks the loop
    elif guess > generated:
        print ("You have guessed too high")
        #addresses the user's guess by giving hint   
    elif guess < generated:
        print ("You have guessed too low")
        #addresses the user's guess by giving hint 
        
if chance >= 10:
    print()
    print ("The number is", generated)
    #once user have tried guessing 10 times, program will display the random generated number
    print ("Better luck next time!")