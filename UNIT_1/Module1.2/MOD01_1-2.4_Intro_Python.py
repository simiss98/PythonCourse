# [ ] get input for a variable, fav_food, that describes a favorite food
fav_food=input("What is your favorite food? Please enter this on a keyboard!")
# [ ] display fav_food as ALL CAPS, used in a sentence
print(fav_food.upper())
# [ ] dispaly fav_food as all lower case, used in a sentence
print(fav_food.lower())
# [] display fav_food with swapped case, used in a sentence
print(fav_food.swapcase())
# [] display fav_food with capitalization, used in a sentence
print(fav_food.capitalize())
fav_color = "Forest Green"
# [] display the fav_color variable as upper, lower, swapcase, and capitalize formatting in a single print() statement
print(fav_color.upper(),fav_color.lower(),fav_color.swapcase(),fav_color.capitalize())
# [] input variable fav_color as upper
fav_color=input("Please enter your favorite color!").upper()
# [] print fav_color
print(fav_color)
# [] print 3 tests, with description text, testing the menu variable for 'pizza', 'soup' and 'dessert'
menu = "salad, pasta, sandwich, pizza, drinks, dessert"
print("Is pizza in the mennu =","pizza" in menu)
print("Is soup in the menu =", "soup" in menu)
print("Is dessert in the menu =","dessert" in menu)
# Create a program where the user supplies input to search the menu
menu1="Salad, soup, DESSERT, PIZzA, bURGER, sanDwIcH, Drinks, pasta, Ice Cream,"
menu_ask=input("What would you like? I will let you know if we have that in the menu!").upper()
print(menu_ask in menu1.upper())
# add to menu Task
#printing current menu
print("This is our current menu: ",menu1.title())
#get user input for add_item variable
add_item=input("Please enter what should be added to the menu!").title()
#creating new variabe which stores, user's input
new_menu=menu1.title()+" "+add_item.title()
#printing updated menu
print("This is our new menu:",new_menu)
#check if an item is on the menu, check for previous items and the item you added
print("Is Brisket in the menu =","Brisket" in menu1)
print("Is",menu1.title(),"in the menu =",menu1.title() in menu1.title())
print("Is", add_item.title(),"in the menu =",add_item.title() in new_menu.title())
#task4
# [ ] fix the error
#paint_colors = "red, blue, green, black, orange, pink"
#print('Red in paint colors = ',red in paint_colors)
paint_colors = "red, blue, green, black, orange, pink"
print('Red in paint colors = ',"red" in paint_colors)