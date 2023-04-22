names = input ("who are all there today? Give names seperated by comma.\n")

name_list = names.split(", ")

import random
choice = random.randint(0,len(name_list)-1)


print(f"{name_list[choice]} is going to buy the meal today!")
