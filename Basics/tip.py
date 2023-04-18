print ("Welcome to the tip calculator")
bill = float(input ("what is the total bill?\n"))
tip = int(input ("what percentage of tip would you like to give? 10,12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))

each_pay = format(round((bill*(1+(tip/100)))/people , 2),'.2f')

print (f"Eac person should pay: ${each_pay}")