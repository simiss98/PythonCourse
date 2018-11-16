#Task1
print("Task1")
# create and call make_doctor() with full_name argument from user input - then print the return value
def make_doctor(name=input("Enter full name")):
    full_name=name.upper()
    return full_name
print(make_doctor())
print()

#Task2
print("Task2")
# [ ] add a 3rd period parameter to make_schedule

def make_schedule(period1, period2, period_3):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title() + ", [3rd] " + period_3.title())
    return schedule
#Adding values for the parameters
student_schedule = make_schedule("mathematics", "history", "biology")
#printing schedule
print("SCHEDULE:", student_schedule)

# [ ] Optional - print a schedule for 6 classes (Tip: perhaps let the function make this easy)
def make_this_easy(period4, period5, period6):
    classes = (", [4th] "+period4.title()+", [5th] "+period5.title()+", [6th] "+period6.title())
    return classes
more_classes= make_this_easy("science","economics","Python")
print("Student's Schedule:",student_schedule+more_classes)