
year = int(input(" Enter Year to Test: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{} is a leap year".format(year))
        else:
            print("{} is not a leap year".format(year))
    else:
        print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))
    
# Erick
# 0740922861
# 5rdqjfe - google classroom
#         - join via code
# N
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