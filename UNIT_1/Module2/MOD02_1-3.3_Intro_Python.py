#Task1
print("Task1")
print()
# [ ] fix the sequence of the code to remove the NameError
def hat_available(color):
    hat_colors = 'black, red, blue, green, white, grey, brown, pink'
    return (color.lower() in hat_colors)
have_hat = hat_available('green')
print('hat available is', have_hat)
#Task2
print("\nTask2")

# [ ] create function bird_available
def bird_available(bird):
    bird_types = 'crow robin parrot eagle sandpiper hawk pigeon'.title()
    return (bird.title() in bird_types)
# [ ] user input
# [ ] call bird_available
has_bird=bird_available(input("Enter a bird type to search"))
# [ ] print availbility status
print('Bird available = ', has_bird)
print("\nTask3")
# define function how_many
def how_many():
    requested = input("enter how many you want: ")
    return requested

# get the number_needed
number_needed = how_many()
print(number_needed, "will be ordered")

print("\nTask3")
# define function how_many
def how_many():
    requested = input("enter how many you want: ")
    return requested
# get the number_needed
number_needed = how_many()
print(number_needed, "will be ordered")
