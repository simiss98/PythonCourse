#Task1
#[ ] increase the number of arguments used in print() to 8 or more
student_age = 17
student_name = "Hiroto Yamaguchi"
next_year = "But next year,"
graduate = "He will be official graduate."
professional = "Then he will start his professional carreer."
print(student_name,'will be in the class for',student_age, 'year old students.',next_year+"","if he study hard.",""+graduate,professional)

#Task2
#[ ] define (def) a simple function called yell_it() and call the function
def yell_it():
    phrase="do not shout"
    print(phrase.upper(),"!")
yell_it()

#Task3

#[ ] define yell_this()
# [ ] get user input in variable words_to_yell
# [ ] call yell_this function with words_to_yell as argument
def yell_this(words_to_yell=input("enter a phrase to yell").upper()):
    print(words_to_yell)
yell_this()