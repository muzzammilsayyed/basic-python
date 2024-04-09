import random
import math
#take inputs
low = int(input("enter Lower bound: "))

up = int(input("enter Upper bound: "))
#generate random num betwee low and up
x = random.randint(low, up)
print("\n\tYOu've only ", round(math.log(up - low +1, 2)),'chances to guess integer\n')

#initialize num guess
count = 0
#for calc of min num of guesses depends on range
while count < math.log(up - low +1, 2):
    count+= 1

    #take guessing num as input
    guess = int(input("Guess a Number: "))

    #condition testing
    if x == guess:
        print("Congratulations you did it in", count, " try")
        break #loop breaks
    elif x > guess:
        print("your guess is too low")
    elif x < guess:
        print("your guess is too high") 
#if guess is more than required guesses, shows output
if count >= math.log(up - low +1, 2):
    print("\nThe number is %d" % x)
    print("\tTry your luck once again")        

