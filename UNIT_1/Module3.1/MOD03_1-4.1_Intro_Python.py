#Task1
print("Task1")
sunny_today = True
# [ ] test if it is sunny_today and give proper responses using if and else
if sunny_today:
    print("It is sunny today")
else:
    print("It is cloudy today")

sunny_today = False
# [ ] use code you created above and test sunny_today = False

if sunny_today:
    print("It is sunny today")
else:
    print("It is cloudy today")
#Task2
print("\nTask2")

test_string_1 = "welcome"
test_string_2 = "I have $3"
# [ ] use if, else to test for islower() for the 2 strings
#testing lower case for test_string_1
if test_string_1.islower():
    print("it is lower case text")
else:
    print("it is not lower case text")
#testing lower case for test_string_2
if test_string_2.islower():
    print("it is lower case word")
else:
    print("it is not lower case word")

if test_string_1.islower() and test_string_2.islower():
    print("both texts are using only lower case letters ")
else:
    print("one of the text includes upper case letter")

test_string_1 = "welcome"
test_string_2 = "I have $3"
test_string_3 = "With a function it's efficient to repeat code"


def w_start_test(text):
    if text.lower().startswith("w"):
        print("\nYes, " + text + " starts with w as a first letter")
    else:
        print("No "+text+" does not start with w")


# [ ] Test the 3 string variables provided by calling w_start_test()
w_start_test(test_string_1)
w_start_test(test_string_2)
w_start_test(test_string_3)
