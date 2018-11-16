#Task1

# [ ] print the result of subtracting 15 from 43
print("subtracting 15 from 43 = ", 43-15)
# [ ] print the result of multiplying 15 and 43
print("multiplying 15 and 43 = ", 15*43)
# [ ] print the result of dividing 156 by 12
print("dividing 156 by 12 = ", 156/12)
# [ ] print the result of dividing 21 by 0.5
print("dividing 21 by 0.5 = ", 21/0.5)
# [ ] print the result of adding 111 plus 84 and then subtracting 45
print("111 plus 84 and then subtracting 45 = ",111+84-45)
# [ ] print the result of adding 21 and 4 and then multiplying that sum by 4
print("(21 plus 4) multiplying sum by 4 = ", (21+4)*4)

#Task2
# [ ] create and test multiply() function
#define function multiply(), and within the function:
#gets user input() of 2 strings made of whole numbers
#cast the input to int()
def multiply(num_1 = int(input("Enter any number")),num_2 = int(input("Enter any number"))):
    test=num_1*num_2
    return test

#print using string type
print(str(multiply()))

#Task3
# [ ] create improved multiply() function and test with /, no argument, and an invalid operator ($)
#update the multiply() function to multiply or divide
#single parameter is operator with arguments of * or / operator
#default operator is "*" (multiply)
#return the result of multiplication or division
#if operator other than "*" or "/" then return "Invalid Operator"

def advanced_multiply(operator=input("Enter * to multiple or / to divide")):

    if operator is "*":
        number1 = int(input("Enter 1st number to divide "))
        number2 = int(input("Enter 2nd number to divide"))
        print("Your result is", number1*number2)
        pass
    elif operator is "/":
        number1 = int(input("Enter 1st number to divide "))
        number2 = int(input("Enter 2nd number to divide"))
        print("Your result is", number1/number2)
        pass
    else:
        print("Invalid operator")

print(advanced_multiply())

#Task4
# Review, run, fix

student_name = input("enter name: ").capitalize()
if student_name.startswith("F"):
    print(student_name,"Congratulations, names starting with 'F' get to go first today!")
elif student_name.startswith("G"):#: is required to end elif statement.
    print(student_name,"Congratulations, names starting with 'G' get to go second today!")
else:
    print(student_name, "please wait for students with names staring with 'F' and 'G' to go first today.")

