#Tasks
# [ ] print a string that outputs the following exactly: The new line character is "\n"
print("The new line character is \"\\n\"")
# [ ] print output that is exactly (with quotes): "That's how we escape!"
print("\"That\'s how we escape!\"")
# [ ] with only 1 print statement and using No Space Characters, output the text commented below
# 1       one
# 22      two
# 333     three
print("1\t\tone\n22\t\ttwo\n333\t\tthree")

# [ ] create and test quote_me()
# test="Hello people".replace("e", "\'")
# print(test)

def quote_me(qoute):
    word=qoute
    #check if passed string starts with a double quote ("\""), then surround string with single quotations
    if word.startswith("\""):
        print(word.replace("\"", "\'"))
        #if the passed string starts with single quote, or
    elif word.startswith("\'"):
        print(word.replace("\'", "\""))
    else:
        #if doesn't start with a quotation mark, then surround with double quotations
        print("\"" + word + "\"")
#Test the function code passing string input as the argument to quote_me()
test = quote_me(input("Enter a word to quote: "))


# [ ] create shirt order using nested if
#First get input for color and size
available =True
White_shirt_L = 200
White_shirt_M = 240
Blue_shirt_L =145
Blue_shirt_M = 400


order = "Welcome to shirt world, please start your order."
print(order)
color = str(input("What color shirt you would like, White or Blue? ")).title()
if color == "White" or color == "Blue":
    print("Thank you, "+color+ " is good decision")
    size = input("What size would you like, L or M: ").title()
    if size == "L" or size == "M":
        print("Thank you for choosing size "+size)
        quantity = int(input("How many shirts would you like? "))
        if color =="White" and size == "L" and quantity <= White_shirt_L:
            print("Checking if", quantity, color, size, "shirts are available = " + str(available))
            print("Thank you for you order"+"\nOrder details:"+"\nShirt color - "+color+"\nSize - "+size+"\nQuantity - "+str(quantity))
        elif color =="White" and size == "M" and quantity <= White_shirt_M:
            print("Checking if", quantity, color, size, "shirts are available = " + str(available))
            print("Thank you for you order"+"\nOrder details:"+"\nShirt color - "+color+"\nSize - "+size+"\nQuantity - "+str(quantity))
        elif color == "Blue" and size == "M" and quantity <= Blue_shirt_M:
            print("Checking if", quantity, color, size, "shirts are available = " + str(available))
            print("Thank you for you order"+"\nOrder details:"+"\nShirt color - "+color+"\nSize - "+size+"\nQuantity - "+str(quantity))
        elif color =="Blue" and size == "L" and quantity <= Blue_shirt_L:
            print("Checking if", quantity, color, size, "shirts are available = " + str(available))
            print("Thank you for you order"+"\nOrder details:"+"\nShirt color - "+color+"\nSize - "+size+"\nQuantity - "+str(quantity))
        else:
            print("I am sorry we do not have",str(quantity),"available.")
    else:
        print("Sorry we do not have size "+size)
else:
    print("Sorry we do not have \""+color+"\" color")

# [ ] create and test str_analysis()
def str_analysis(str_input):
    test = str_input
    # Check if string is digits
    # if digits: convert to int and check if greater than 99
    if test.isdigit() and int(test) > 99:
        print("Checking if entered string includes digits only := ", test.isdigit())
        # if greater than 99, print a message about a "big number"
        print("\nYour number is greater than 99")
    elif test.isdigit() and int(test) < 99:
        # if not greater than 99, print message about "small number"
        print("\nYour number is smaller than 99")
        # if not digits: check if string isalpha
    elif test.isalpha():
        # if isalpha print message about being all alpha
        print("Your string includes alphabetical characters only")
    else:
        # if not isalpha print a message about being neither all alpha nor all digit
        print("Your entered string is not all alpha and is not all digits")


# [ ] create and call ticket_check()

def ticket_check(section):
    # string and expects: general, floor
    # if section is general( or use startswith "g")
    # if section is floor( or use starts with "f")
    if (section.startswith("G") or section.startswith("F")) and (section == "General" or section == "Floor"):
        print("Thank for choosing "+section+" section")
        seat = input("Enter a seat number"+"\nFor General Section 1 - 10"+"\nFor Floor section 1 - 4 " )
        # integer and expects: 1 - 10
        # if seats is 1 - 10 return True
        if seat.isdigit() and int(seat) >= 1 and int(seat) <= 10 and section == "General":
            print("Seat " + seat + " is available")
            # if seats is 1 - 4 return True
        elif seat.isdigit() and int(seat) >= 1 and int(seat) <= 4 and section == "Floor":
            print("Seat " + seat + " is available")
        else:
            #IF seat is outside seat range
            print("There is no seat \""+seat+"\" in the section ",section)
    else:
        # IF section is not general or floor
        print("There is no "+section+" section")




call = ticket_check(input("Enter a section General or Floor: ").title())