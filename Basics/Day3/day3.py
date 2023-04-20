# print ("Welcome to Rollercoaster!!")

# height = int(input("What is your height?\n"))

# if height > 120:
#     print ("you can ride the rollercoaster!:-)")
# else:
#     print ("Sorry, you have to grow taller before you can ride :-( :-( :-()")


# # # comparison operater
# # # <
# # # >
# # # <=
# # # >=
# # # ==
# # # !=
# # # % (modulo)

# height1 = float(input("What is your height?\n"))
# age = int(input("What is your age?\n"))

# if height1 > 120:
#     if age >= 18:
#         print ("Please pay $12")
#     elif age <= 12:
#         print ("Please pay $5")
#     else:
#         print ("please pay $7")
# else:
#     print ("Sorry, you have to grow taller before you can ride :-( :-( :-()")


print ("Welcome to Rollercoaster!!")

height = int(input ("what is your height in cm?\n"))
age = int(input ("what is your age?\n"))
bill = 0
if height > 120:
    if age >= 45 and age <= 55:
        bill = 0
        print ("You can ride without any cost!!")
    elif age > 18:
        bill = 12
        print ("Adult ticket will cost $12")
    elif age > 12:
        bill = 7
        print ("Teen tickets will cost $7")
    else:
        bill = 5
        print ("children ticketr will cost $5")
    
    photo = input("Do you want photo? Y or N")

    if photo == "Y":
        if age >= 45 and age <= 55:
            bill += 0
        else:
            bill += 3
    print (f"your final bill is ${bill}")

else:
    print ("Sorry you need to grow up a little more to ride !!")