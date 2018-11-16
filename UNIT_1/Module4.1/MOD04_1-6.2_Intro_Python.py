#Task1
# [ ] print "\\\WARNING!///"
print("\\\\\\WARNING!///")
# [ ] print output that is exactly (with quotes): "What's that?" isn't a specific question.
print("\nWhat\'s that?\" isn\'t a specific question.")
# [ ] from 1 print statement output the text commented below using no spaces
# One     Two     Three
# Four    Five    Six
print("\nOne\t\tTwo\t\tThree\nFour\tFive\tSix")


#test = input("Enter a word that starts with \"pre\": ").lower()

#task2
# [ ] create and test pre_word()

def pre_word(word):
    #Check if word starts with "pre" and  Check if word .isalpha()
    test = (word.isalpha() and word.startswith("pre"))
    if test:
        #if all checks pass: return True
        return True
    else:
        #if any checks fail: return False
        return False
#get input using the directions: *enter a word that starts with "pre": *
#call pre_word() with the input string
check_word=pre_word(input("Enter a word that starts with pre: ").lower())
if check_word is False:
    #test if return value is False and print message explaining not a "pre" word
    print("\nWord does not start with pre")
else:
    #else print message explaining is a valid "pre" word
    print("\nWord start with pre")

#Task5 ?
# [ ] review, run, fix
#print("Hello" + \n + "World!")
print()
print("Hello" + "\nWorld!")

