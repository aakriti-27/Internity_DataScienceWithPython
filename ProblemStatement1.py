'''Create a python program in which the user selects a particular
range of number (example 20 to 80 or 330 to 430). The system
should automatically select some random number and the user
must identify that number selected by the system in minimum number of guesses.

If the user identifies it in the required number of guesses then it
should print "Yeah! You identified the number"

else if the number guessed by the user is higher than the randomly
selected number then it should print
"Please try again! The number you guessed is too high"

else if he number guessed by the user is smaller than the randomly
selected number then it should print
"Please try again! The number you guessed is too small".

Else if the user does not guess the integer in minimum number of guesses, then it should
give "Oops! All you chances are finished. Better luck next time!"
'''

import random

while(True):
    try:
        range = input("Please enter the range in the given format (Format => '20 to 80') : \n")
        n1 = int(range[:(range.find(' ')+1)])    #to extract smallest value of range
        n2 = int(range[(range.rindex(' ')):])    #to extract largest value of range
        break
    except:
        print("Invalid input! Please enter in correct format.")

r = random.randint(n1, n2)   #to generate a random number in the given range

print("\nYou will be given 3 chances to guess the number\n ----Let's get started----\n")

count=1

while(True):

    while(True):
        try:
            num = int(input("Chance {} : Guess the number\n".format(count)))
            break
        except:
            print("Invalid input! Please enter a integer")
        
    if (num !=r and count == 3):
        print("Oops! All you chances are finished. Better luck next time!")
        break
    elif (num == r):
        print("Yeah! You identified the number.")
        break
    elif (num > r):
        print("Please try again! The number you guessed is too high.")
    elif (num < r):
        print("Please try again! The number you guessed is too small.")
    
    count=count+1


#Output- Use Case 1:
'''Please enter the range in the given format (Format => '20 to 80') : 
20-80
Invalid input! Please enter in correct format.
Please enter the range in the given format (Format => '20 to 80') :
20 to 80

You will be given 3 chances to guess the number
 ----Let's get started----

Chance 1 : Guess the number
34
Please try again! The number you guessed is too high.
Chance 2 : Guess the number
23
Please try again! The number you guessed is too small.
Chance 3 : Guess the number
30
Oops! All you chances are finished. Better luck next time!
'''

#Output- Use Case 2:
'''
Please enter the range in the given format (Format => '20 to 80') :
110 to 115

You will be given 3 chances to guess the number
 ----Let's get started----

Chance 1 : Guess the number
114
Please try again! The number you guessed is too high.
Chance 2 : Guess the number
one hundred twelve
Invalid input! Please enter a integer
Chance 2 : Guess the number
112
Please try again! The number you guessed is too small.
Chance 3 : Guess the number
113
Yeah! You identified the number.
'''

