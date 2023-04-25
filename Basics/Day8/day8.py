# positional argument - more than one paramenter and argument
# we should not change the order

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

position = alphabet.index("a")

newpos = position - 5
print (newpos)
print (alphabet[newpos])

def greet(name, location):
    print (f"Hello {name}")
    print (f"Good Morning")
    print (f"Have a nice day {name}")
    print (f"how is it in {location}?")

greet("manoj", "Vellore")


#keyword argument

def sum_num(a,b,c):
    z= a+b+c
    print (f"a is {a}, b is {b}, c is {c}")
    print(f"sum is: {z}")

sum_num(a=1,c=3,b=5)