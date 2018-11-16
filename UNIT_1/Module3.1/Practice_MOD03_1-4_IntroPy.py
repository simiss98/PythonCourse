# [ ] input a variable: age as digit and cast to int
age=int(input("Enter age"))
#print(type(age))
# if age greater than or equal to 12 then print message on age in 10 years
if age >=12:
    print('you will be',age+10,"in 10 years")
# or else print message "It is good to be" age
else:
    print("It is good to be", age)
    # [ ] input a number


    number=input("Enter a number: ")
    # if number IS a digit string then cast to int
    if number.isdigit():
        print(type(int(number)))
        # print number "greater than 100 is" True/False
        print("Checking if number is greater than 100:= ", int(number) > 100)
        # if number is NOT a digit string then message the user that "only int is accepted"
    else:
        print("entered number is not a digit, Please enter only a digit")

        guess_input = "Enter your guess"
        letter = "A".capitalize()
print()
guess_input="Enter your guess"
# [ ] create check_guess()
def check_guess(guess):
            # [ ] call check_guess with user input
            test_input = input(guess_input).capitalize()
            if test_input == guess:
                print("your guess is correct")
            else:
                print("your guess is incorrect")
# call with test
test = check_guess("A")






# [ ] create letter_guess() function, call the function to test

# [ ] create check_guess()
def check_guess(correct_value):
    for chance in range(3):
        guess = input("What is your guess").title()
        if guess == correct_value:
            return True
        else:
            pass
    return False

#creating a value for true and printing a response of guess

if check_guess("A".title()):
    print("Correct")
else:
    print("Not a single value is correct")
    pass



# [ ] complete pet conversation

#ask the user for a sentence about a pet and then reply
#get user input in variable: about_pet

about_pet=input("Enter a few animals you like ").title()
def checkanimal(animal):
    # using a series of if statements respond with appropriate conversation
    # check if "dog" is in the string about_pet (sample reply "Ah, a dog")
    if animal.title() in about_pet:
        print("Ah a "+animal)
    else:
        pass

test=checkanimal("dog".title())
tet=checkanimal("cat".title())

print("Thank you for your story.")