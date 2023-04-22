rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

map = [rock,paper,scissors]

user = int(input("Type 0 for Rock, 1 for Paper , 2 for Scissors\n"))

print ("\n\n")
print ("You chose")

print (map[user])

import random

computer = random.randint(0,2)
print ("\n")
print ("Computer chose")

print (map[computer])

if user == 0 and computer == 1:
    print ("You Lose")
elif user == 0 and computer == 2:
    print ("You Won")
elif user == 1 and computer == 2:
    print ("You Lose")
elif user == 1 and computer == 0:
    print ("You Won")
elif user == 2 and computer == 0:
    print ("You Lose")
elif user == 2 and computer == 1:
    print ("You Won")
else:
    print ("It is a Draw!!")