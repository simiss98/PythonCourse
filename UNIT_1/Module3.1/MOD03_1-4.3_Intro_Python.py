#Task1
msg = "Hello"
# [ ] print the True/False results of testing if msg string equals "Hello" string

print("check if msg = Hello : ",msg=="Hello")
greeting = "Hello"
# [ ] get input for variable named msg, and ask user to 'Say "Hello"'
named_msg=input("Enter your name: ").capitalize()
print(named_msg, "Say",greeting)
# [ ] print the results of testing if msg string equals greeting string
if msg==greeting:
    print("\nmsg variable is equal to greeting variable")
else:
    print("\n",msg," and ",greeting," words are different")
print()

#Task2
# [ ] get input for a variable, answer, and ask user 'What is 8 + 13? : '
answer=input("What is 8 + 13?")
# [ ] print messages for correct answer "21" or incorrect answer using if/else
if answer =="21":
    print("Correct answer is 21")
else:
    print("Incorrect try again")
# note: input returns a "string"

#Task3

#tf_quiz() has 2 parameters which are both string arguments
#question: a string containg a T/F question like "Should save your notebook after edit?(T/F): "
#correct_ans: a string indicating the correct answer, either "T" or "F"
#tf_quiz() returns a string: "correct" or "incorrect"
#Test tf_quiz(): create a T/F question (or several!) to call tf_quiz()


# [ ] Create the program, run tests
question = "Should save your notebook after edit? (T/F): "
correct_ans = "T"
def tf_quiz(question, correct_ans):
    answer = input(question)
    if answer == correct_ans:
        return "correct"
    else:
        return "incorrect"
#print(tf_quiz(question, correct_ans))

quiz_eval = tf_quiz("Should save your notebook after edit?(T/F):","T")
print("your answer is",quiz_eval)