# Network: Modcom Institute
# Password: modcom1234

# DESKTOP
# eight zeros -> 00000000
# Conditions
# Single Alternative -> if
# Double Alternative -> if..else
# Multiple Alternative -> elif

# Python Loops
# while loop
# for loop

# functions

# multiple alternative -> More than one condition
# Grading Systems
# 0 - 40 -> E
# 41 - 50 -> D
# 51 - 60 -> C
# 61 - 70 -> B
# 70 - 100 -> A
# Less than 0 and More than 100 -> Invalid

# Logical Operators -> and, or, not
# and -> Both
# or -> Either
# not -> Opposite
# score > 0 and score <=40

score = int(input(" Enter Your Score : "))
if 0 < score <= 40:
    print("Your Score is E")
elif score >= 41 and score <=50:
    print("Your Score is D")
elif score >=51 and score <=60:
    print("Your Score is C")
elif score >=61 and score <=70:
    print("Your Score is B")
elif score >=71 and score<=100:
    print("Your Score is A")
else:
    print("Invalid Score")


