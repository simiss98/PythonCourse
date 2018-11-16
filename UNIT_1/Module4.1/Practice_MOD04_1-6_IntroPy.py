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
color = str(input("What color shirt you would like, White and Blue? ")).title()
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