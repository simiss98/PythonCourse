# [ ] get user input for a variable named remind_me
remind_me=input("Please remind me what is your name? ").capitalize()
# [ ] print the value of the variable remind_me
print("Hello",remind_me)
# use string addition to print "remember: " before the remind_me input string
print("remember: "+"before the "+remind_me+" input string")
# [ ] get user input for 2 variables: meeting_subject and meeting_time
meeting_subject=input("what is the meeting subject?:").capitalize()
meeting_time=input("what is the meeting time?:")
# [ ] use string addition to print meeting subject and time with labels
print("Meeting Subject: "+meeting_subject)
print("Meeting Time:    "+meeting_time)
# [ ] print the combined strings "Wednesday is" and "in the middle of the week"
print("Wednesday is","in the middle of the week")
# [ ] print combined string "Remember to" and the string variable remind_me from input above
print("Remember to",remind_me)
# [ ] Combine 3 variables from above with multiple strings
print("Hello",remind_me+",","Please remember that meeting is scheduled for",meeting_subject,"at",meeting_time)
# [ ] print a string sentence that will display an Apostrophe (')
print("'I forgot that Michael's Birthday was on Monday'".upper())
# [ ] print a string sentence that will display a quote(") or quotes
print('I am very "lazy".')

#get user input for a variable named vehicle
#bonus print description for each test (e.g.- "All Alpha: True")
vehicle=input("What is your favorite vehicle?")
#check True or False if vehicle is All alphabetical characters using .isalpha()
print("vehicle name consist of alphabetical characters only: =",vehicle.isalpha())
#check True or False if vehicle is only All alphabetical & numeric characters
print("vehicle name consist of alphabetical or numeric characters: =",vehicle.isalnum())
#check True or False if vehicle is Capitalized (first letter only)
print("vehicle name start with capital letter: =",vehicle.istitle())
#check True or False if vehicle is All lowercase
print("vehicle name consist of all lower case letters: =",vehicle.islower())
# [ ] print True or False if color starts with "b"
print("color".startswith("b"))

# [ ] print the string variable capital_this Capitalizing only the first letter
capitalize_this = "the TIME is Noon."
print(capitalize_this.capitalize())
# print the string variable swap_this in swapped case
swap_this = "wHO writes LIKE tHIS?"
print(swap_this.swapcase())
# print the string variable yell_this in all UPPERCASE
yell_this = "Can you hear me Now!?"
print(yell_this.upper())
#format input using .upper(), .lower(), .swapcase, .capitalize()
format_input = input('enter a string to reformat: ')
print(format_input.upper(),format_input.lower(),format_input.swapcase(),format_input.capitalize())

# [ ] get user input for a variable named color
color=input("What is your favorite color?")
# [ ] modify color to be all lowercase and print
print(color.lower())

# [ ] get user input using variable remind_me and format to all **lowercase** and print
remind_me=input("What do you need to remember?").lower()
print(remind_me)
# [ ] test using input with mixed upper and lower cases
remind_me=input("What do you need to remember?").lower()
print(remind_me.upper())
remind_me=input("What do you need to remember?").upper()
print(remind_me.lower())
# [] get user input for the variable yell_this and format as a "YELL" to ALL CAPS
yell_this=input("What we need to know?").upper()
print(yell_this)

# [ ] get user input for the name of some animals in the variable animals_input
animals_input=input("Please enter 3 animals you like the most: ").title()
# [ ] print true or false if 'cat' is in the string variable animals_input
print("Is cat in this list =","cat".capitalize() in animals_input)

# [ ] get user input for color
color=input("Enter any color")
# [ ] print True or False for starts with "b"
print("Maybe this color starts with letter b:= ",color.startswith("b"))
# [ ] print color variable value exactly as input
#print(color)
#     test with input: "Blue", "BLUE", "bLUE"
if color.startswith("b"):
    print("Color starts with letter b")
else:
    print("Color does not start with b")

    # project: "guess what I'm reading"

    # 1[ ] get 1 word input for can_read variable
    can_read = input("Enter 1 word item that can be read:")
    # 2[ ] get 3 things input for can_read_things variable
    can_read_things = input("Enter 3 items that can be read:")
    # 3[ ] print True if can_read is in can_read_things
    print("Checking if 1 word item is in the 3 items list :=", can_read.lower() in can_read_things.lower())
    # [] challenge: format the output to read "item found = True" (or false)
    # hint: look print formatting exercises
    print("item found =", can_read.lower() in can_read_things.lower())

# Allergy check

# 1[ ] get input for test
input_test=input("Enter something eaten in the last 24hrs").title()
# 2/3[ ] print True if "dairy" is in the input or False if not
print("It is","dairy".title() in input_test,"that",input_test,'contains "dairy"')
# 4[ ] Check if "nuts" are in the input
print("It is","nuts".title() in input_test,"that",input_test,'contains "nuts"')
# 4+[ ] Challenge: Check if "seafood" is in the input
print("It is","seafood".title() in input_test,"that",input_test,'contains "seafood"')
# 4+[ ] Challenge: Check if "chocolate" is in the input
print("It is","chocolate".title() in input_test,"that",input_test,'contains "chocolate"')