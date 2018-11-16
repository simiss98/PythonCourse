print("\nTasks")
# [ ] define and call a function short_rhyme() that prints a 2 line rhyme
def short_rhyme(rhyme="It's hard to see the butterfly \n Because he flies across the sky"):
    return rhyme
print("\n",short_rhyme())

# [ ] define (def) a simple function: title_it() and call the function
# - has a string parameter: msg
# [ ] get user input with prompt "what is the title?"
def title_it(msg=input("\nwhat is the title?")):
    return msg
# - prints msg in Title Case
print(title_it().title())
# [ ] call title_it() using input for the string argument
calling_title_it=title_it()
# [ ] define title_it_rtn() which returns a titled string instead of printing
def title_it_rtn(string="This is a string to return"):
    return string.title()
# [ ] call title_it_rtn() using input for the string argument and print the result
calling_title_it_rtn=title_it_rtn(input("\nEnter a book title on a keyboard!"))
print(calling_title_it_rtn)
# [ ] create, call and test bookstore() function
def bookstore(book=calling_title_it_rtn,price=input("\nEnter a book price on a keyboard!")):
    Title="Title: "+book+", costs $"+price
    return Title
print(bookstore())

#Fix the error

def get_name():
    name_entry = input("enter a name: ")
    return name_entry

def get_greeting():
    greeting_entry = input("enter a greeting: ")
    return greeting_entry

def make_greeting(name, greeting = "Hello"):
    return (greeting + " " + name + "!")

# get name and greeting, send to make_greeting
print(make_greeting(get_name(), get_greeting()))