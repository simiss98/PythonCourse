#Task1

# [ ] Say "Hello" with nested if
# [ ] Challenge: handle input other than y/n

print("Please Say Hello")
hello_decision=input('"y" for yes or "n" for no: ' )
print()
#1st nested if
if hello_decision.lower()=="y":
#select hello type
    print("Please select hello type.")
    hello_type = input('"hello" for full hello or "hi" for Hi ')
    print()
    #2nd nested if elif else
    if hello_type.lower() =="hello":
            print("Say Hello.  Thank you.")
    elif hello_type.lower() == "hi":
            print("Say hi. Thank you.")
    else:
            print("Sorry there is no such a hello type as ",hello_type, "Thank you.")
# still first nested elif else
elif hello_decision.lower() == "n":
    print("Friendly nod")
else:
    print("Sorry we do not understand your decision by,", hello_decision, "choice.")
print()
print("Good bye!")
print()
#Task2
# [ ] Create the "Guess the bird" program
print("Hello, guess what bird is my favorite, you have 3 attempts!")
correct_bird="Eagle"
def guess_bird(bird):
    if bird.title() == correct_bird:
        print("Yes you are right!")
    elif bird.title() !=correct_bird:
        print("That is incorrect try again, 2 attempts left")
        print()
        guess_2=input("Enter your 2nd guess").title()
        if guess_2 == correct_bird:
            print("Yes you are right!")
        elif guess_2.title() != correct_bird:
            print("Sorry you are wrong, try again")
            print()
            guess_3= input("3rd and last attempt, Good luck!").title()
            if guess_3 == correct_bird:
                print("Yes you are right!")
            elif guess_3 != correct_bird:
                print("You are wrong, but thanks for trying.")
            else:
                print("I do not understand your input")
        else: print("I do not understand your input")

    else:
        print("I do not understand what you mean")


print(guess_bird(bird=input("You have 3 attempts enter your 1st guess")))