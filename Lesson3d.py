# Loops in Collections
# Lists
# continue -> skip values on a loop
# break -> Breaks a for loop

courses = ["BBIT", "IT", "Software Eng.", "CS", "IS"]
for course in courses:
    if course == "CS":
        break
    print(course)
