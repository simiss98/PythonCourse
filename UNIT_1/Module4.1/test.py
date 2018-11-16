#test="Hello people".replace("e", "\'")
#print(test)


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
White_shirt_L = 400
White_shirt_M = 400
Blue_shirt_L =400
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
            print("I am sorry we have only",str(White_shirt_L),"available.")
    else:
        print("Sorry we do not have size "+size)
else:
    print("Sorry we do not have \""+color+"\" color")