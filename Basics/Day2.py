# we cannot calculate length of int so we need to convert it into string
# there are two options in doing that one is putting the int within ""
# another is giving them within str function

print(len("123456"))

# we can use subscript to pull the character from string

print("hello"[4]) #this will print 'o' from "hello"

# string will always are between "" int will not have ""

print("123"+"345")

print(123+345)

# int can be written with _ between them this is substitute for , as to write large intiger.
# computer will not take it is for our convineence

print(123_456_789)

# int are whole numbers
# decimal are float

print(3.456+1.234)

# boolean is either true or false. It will not have ""

print(True)
print(False)

# to find the type of data we can use type

print(type(123))
print(type("123"))
print(type(123.00))
print(type(str(123)))

print(str(123)[1])

print((3 * (3 + 3) / 3 - 3)**2)


print ( round(2.6666666 , 2)) #round to two decmal places

print (8 // 3) # this is floor division just gives the whole number, chops off the decimal

# if we need to print different data types as one string instead of converting data type
# and concortinating it we can use f string

score = 120
height = 1.8
iswinning = True
print (f"score is {score} and your height is {height}. Your winning is {iswinning} ") 