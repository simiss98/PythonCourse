#Task1
print("\nTask1")
# [ ] code and test SHIRT SALE
#Get user input for variable size (S, M, L)
size=input("Enter size: S, M, L - ").upper()
#reply with each shirt size and price (Small =  6,𝑀𝑒𝑑𝑖𝑢𝑚=  7, Large = $ 8)
if size == "S":
    print("Small = $6")
elif size == "M":
    print("Medium = $7")
elif size =="L":
    print("Large = $8")
#optional: add additional sizes
elif size == "XL":
    print("Extra Large = $9")
elif size == "XS":
    print("Extra Small = $5")
#if the reply is other than S, M, L, give a message for not available
else:
    print("Sorry,",size," is not available")

#Task2
print("\nTask2")
str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# [ ] Add the 3 numbers as integers and print the result
print("Sum = ",int(str_num_1)+int(str_num_2)+int_num_3)


# [ ] code and test: adding using int casting
#[ ] initialize str_integer variable to a string containing characters of an integer (quotes)
str_integer = '2'
#[ ] initialize int_number variable with an integer value (no quotes)
int_number = 10
#[ ] initialize number_total variable and add int_number + str_integer using int casting
number_total = int(str_integer) + int_number
#[ ] print the sum (number_total)
print("Sum  = ",number_total)
#Task3
# [ ] code and test the adding calculator
#get input of 2 integer numbers
#cast the input and print the input followed by the result
num_1=int(input("Enter 1st number"))
num_2=int(input("Enter 2nd number"))
#Output Example: 9 + 13 = 22
sum=num_1+num_2
print("Sum of both numbers = ",sum)
#Optional: check if input .isdigit() before trying integer addition to avoid errors in casting invalid inputs
