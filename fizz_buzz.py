# Author: Mengyue Lu
# Date Created: 05/21/2022
# Date Last Modified: 05/23/2022
# Summary: This program will ask the user to enter a number, for every integer divisible by 3
#          the program will instead output "Fizz", for every integer divisible by 5 the program
#          will output "Buzz", if the number can be divisible by both 3 and 5 it will output 
#          "FizzBuzz"
# Method: Using a range based for loop based on the user input, I will be calculating the numbers
#         divisible by 3, 5, and both using the modulo operator.
# Abstract: user_min_input and user_max_input is the range in which the for loop will operate
#           the if and elif conditions check if the nth variable is divisible, otherwise it will
#           print the number

user_min_input = int(input("Enter a minimum number: "))
user_max_input = int(input("Enter a maximum number: "))

for n in range(user_min_input, user_max_input + 1):
    if(n % 3 == 0) and (n % 5 == 0): 
        print("FizzBuzz")
    elif(n % 3 == 0):
        print("Fizz")
    elif(n % 5 == 0):
        print("Buzz")
    else:
        print(n)
    

    