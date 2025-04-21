# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry you have to grow taller before you can ride.")

weight = int(input("What is your weight? "))
height =  float(input("What is your height in m? "))
bmi = weight/(height*2)

if bmi <18.5:
    print("underweight")
elif bmi >=18.5:
    print("normal weight")
elif bmi <25:
    print("normal weight")
else:
    print("overweight")