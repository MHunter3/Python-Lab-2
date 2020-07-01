#CIS 117 Python Programming Lab #2
#Lab #2 - Assigning Variables and Commputing values
#Application - Use student data form user input
"""Description: Create program that computes and displays algebraic expressions
from user data """

#Development Env: Pycharm
#Version: Python 3.7
#file source. morganhunterlab2.py
#Date 6/30/2020

"""
Commented out copy of program run
Enter your family name:Hunter
Enter your student ID number: 01240686
my_id is:  1539301750596
num_let is: 6
expression 1:  620343.00
expression 2:  0
expression 3:  11
expression 4:  1240692
expression 5: 1240680
expression 6:  1121.00
expression 7:  0
expression 8:  1
expression 9:  3.00
False! Expression 8 is not less than expression 7
[1539301750596, 6, 620343.0, 0, 11, 1240692, 1240680, 1121.7775768535262, 0, 1, 3.1]
2020-06-30

Process finished with exit code 0

"""
import math
from datetime import date

family_name = input("Enter your family name:" ) #get family name and store in family_name
my_id = int(input("Enter your student ID number: ")) #get student id and store in my_id

#Begin Validation Functions
def checkName(family_name):
    """
       return errors for min, max char for family_name variable
       :rtype: object
       """
    if family_name < str(2):
        print("Family name must be more than 2 characters")
    elif family_name < str(15):
        print("Family name must be less than 15 characters")

#check calculation function
def checkValidation(my_id):
    """
       return errors for calculation for my_id variable
       :rtype: object
       """
    if my_id == int(1):
        pass
    elif my_id < int(15):
        print("Student ID must be more than 0")

student_id = [] #create empty from user input and store in student_id
for i in range(my_id): #iterate through the list of number from user input
    info = my_id
    student_id.append(my_id)

checkName(family_name) #checkName function call to check family_name 2< or >15
checkValidation(my_id) #checkValidation function call to check my_id <> 0

sum_of_list = sum(student_id) #perform sum function to calculate user input
print("my_id is: " + " " + str(sum_of_list)) #print sum_of_list as a string

num_let = len(family_name) #calculate length of family name and store in num_let
print("num_let is: "  + str(num_let)) #print num_let as a string

# Below are the algebraic expressions using variables
div = my_id / 2 #my_div / 2 stored in div then print div
print("expression 1: " + " " + "{:.2f}".format(int(div)))

mod_my_id = my_id % 2 #my_div % 2 stored in mod_my_id then print mod_my_id
print("expression 2: " + " " + str(mod_my_id))

elips_sum = 2 + 3 + num_let #ellips sum + num_let variable and print elips_sum
print("expression 3: " + " " + str(elips_sum))

main_vars = my_id + num_let #add both main variables store in main_vars and print
print("expression 4: " + " " + str(main_vars))

abs_value = abs(num_let-my_id) #get absolute value of both main variables, store and print in abs)value
print("expression 5: " + "" + str(abs_value))

div_two = (my_id) / (num_let + 1100) #divide my_id by num_let + 1100 store in div_two and print
print("expression 6: " + " " + "{:.2f}".format(int(div_two)))

add_main_vars = (num_let % num_let) and (my_id * my_id) #add both main vars with arithmetic
print("expression 7: " + " " + str(add_main_vars))

div_three = 1 or (my_id/0) #divide my_id by zero and store in div_three and print result
print("expression 8: " + " " + str(div_three))

round_var = round(3.15, 1) #use the round function to round number and store in round_var
print("expression 9: " + " " + "{:.2f}".format(int(round_var)))

def testValues(true, false):
    """
    return boolean value for add_main_vars and div_three
    :rtype: object
    """
    if add_main_vars > div_three:
       print("True! Expression 7 is greater than expression 8")
    else:
        print("False! Expression 8 is not less than expression 7")

testValues(add_main_vars, div_three) #function call to test boolean values for expression 7 and 8

#Assign Expressions results to a list
expressions = [sum_of_list, num_let, div, mod_my_id, elips_sum, main_vars, abs_value,
               div_two, add_main_vars,
               div_three, round_var] #create empty list for expression results
print(expressions)

today = date.today() #current date of program runtime
print(today)



