# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

cname1 = name1.lower()+name2.lower()

x = 0
y = 0

x += cname1.count("t")
x += cname1.count("r")
x += cname1.count("u")
x += cname1.count("e")

y += cname1.count("l")
y += cname1.count("o")
y += cname1.count("v")
y += cname1.count("e")

z = int(str(x)+str(y))

if z<10 or z>90:
    print (f"Your score is {z}, you go together like coke and mentos.")
elif z>=40 and z<=50:
    print (f"Your score is {z}, you are alright together.")
else:
    print (f"Your score is {z}.")