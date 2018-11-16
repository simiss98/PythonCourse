# [ ] create, call and test
# then PASTE THIS CODE into edX
def order_price(weight):
    # set values for maximum and minimum order variables
    maximum = 1000.000
    minimum = 0.100
    # set value for price variable
    price = 7.99
    # check order_amount and give message checking against over maximum under minimum
    if weight < maximum and minimum < weight:
        # else within maximum and minimum give message with calculated price
        print("Your order costs $", price * weight)
    elif weight > maximum:
        print(weight, " is more than currently available")
    elif weight < minimum:
        print(weight, " is below minimum order amount")
    else:
        print("not sure what is your weight")

# get order_amount input and cast to a number
print(order_price(weight=float(input("Enter cheese order weight: example 0.400"))))
