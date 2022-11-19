# For Loop -> Simplified
# for in a range
# Looping a collection

# Range Function, range(), by default accepst the limit
# Start, inc/decre
# start 10
# interval 2
# e,g 10, 12...20
# range(), 1st start, second limit, 3rd inc/dec
for values in range(10, 20, 2):
    print(values)

# for patients in range(10):
#
#     weight = int(input(" Enter Weight: "))
#     height = float(input("Enter Height: "))
#
#     bmi = weight/ (height * height)
#     print("Your BMI is {}".format(bmi))

while True:
    weight = int(input(" Enter Weight: "))
    height = float(input("Enter Height: "))

    bmi = weight / (height * height)
    print("Your BMI is {}".format(bmi))


