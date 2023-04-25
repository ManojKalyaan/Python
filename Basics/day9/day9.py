programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}

print (programming_dictionary["Function"])

for k in programming_dictionary:
    print (k)
    print (programming_dictionary[k])

programming_dictionary["loop"] = "go aroung a set of codes again and again using a set condition"

print ("\n\n\n")
print(programming_dictionary["loop"])

programming_dictionary = {}

print (programming_dictionary)

travel_log = {
  "France": {
    "Paris":4, 
    "Lille":2, 
    "Dijon":1},
  "Germany": {
    "Berlin":1, 
    "Hamburg":3, 
    "Stuttgart":2},
}

travel_log = {
  "France": {"cities_visited" : ["Paris", "Lille", "Dijon"] , "total_visit" : 12},
  "Germany": {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"] , "total_visit" : 2},
}

#dictonary inside list
travel_log = [
{"country_visited" : "France" , "cities_visited" : ["Paris", "Lille", "Dijon"] , "total_visit" : 12},
{"country:visited" : "Germany" , "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"] , "total_visit" : 2},
]



