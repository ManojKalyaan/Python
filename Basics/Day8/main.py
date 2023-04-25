from os import system
import art
cont = True

def encrypt(etext,eshift,edir):
    enc = ""
    eprocess = "encoded"
    if edir == "decode":
        eshift = (eshift*(-1))
        eprocess = "decoded"
    for letter in etext:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_letter = alphabet[position+eshift]
            enc += new_letter
        else:
            enc += letter
    print (f"\n\n\nThe {eprocess} message is \n{enc}")

# def decrypt(etext,eshift):
#     dc = ""
#     for letter in etext:
#         position = alphabet.index(letter)
#         new_letter = alphabet[position-eshift]
#         dc += new_letter
#     print (f"\n\n\nThe decoded message is \n{dc}")



while cont == True:

    system('clear')

    print (art.logo)

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    
    while (direction != "encode") and (direction != "decode"):
        direction = input("please enter the correct value encode/decode\n")
        
    text = input("\n\nType your message:\n").lower()
    shift = int(input("\n\nType the shift number:\n"))

    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    encrypt(etext=text,eshift=(shift%26),edir=direction)

    # if direction == "encode":
    #     encrypt(etext=text,eshift=(shift%26))
    # if direction == "decode":
    #     decrypt(etext=text,eshift=(shift%26))

    restart = input("\n\n\ndo you want to start again? (Y/N)\n").upper()


    if restart == "N":
        cont = False
    
    system('clear')
