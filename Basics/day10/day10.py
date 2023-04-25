def name_calc (f_name,l_name):
    if f_name == "" or  l_name == "":
        return "You didnt provide proper input"
    return  (f'''your name is {f_name.title()+" "+l_name.title()}''')

f_name = input ("first name ?\n")
l_name = input ("last name? \n")

name = name_calc (f_name,l_name)

print(name)