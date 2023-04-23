from os import system
cont = True
while cont == True:

    system('clear')

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    def encrypt(etext,eshift):
        enc = ""
        for letter in etext:
            position = alphabet.index(letter)
            new_letter = alphabet[position+eshift]
            enc += new_letter
        print (f"The encoded message is {enc}")

    def decrypt(etext,eshift):
        dc = ""
        for letter in etext:
            position = alphabet.index(letter)
            new_letter = alphabet[(26+position)-eshift]
            dc += new_letter
        print (f"The decoded message is {dc}")


    if direction == "encode":
        encrypt(etext=text,eshift=shift)
    if direction == "decode":
        decrypt(etext=text,eshift=shift)

        #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
        #e.g. 
        #plain_text = "hello"
        #shift = 5
        #cipher_text = "mjqqt"
        #print output: "The encoded text is mjqqt"

        ##HINT: How do you get the index of an item in a list:
        #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

        ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

    #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

    restart = input("do you want to start again? (Y/N)\n").upper()


    if restart == "N":
        cont = False
