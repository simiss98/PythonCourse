# [ ] create, call and test fishstore() function
def fishstore(fish=input("Entery Fish type on a keyboard ").capitalize(),price=input("Enter fish price on a keyboard ")):
    fish_and_price="Fish Type: "+fish+" costs $"+price
    return fish_and_price
print(fishstore())