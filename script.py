import base64
from art import *

text = text2art("Made by mrpol")
print(text)

check = True
while check == True:

    entry = input("""Choose an option (Type a number):
                        (1) --> Base16 
                        (2) --> Base32
                        (3) --> Base64 
                        (4) --> Exit...
                                """)

    if entry == "1":
        check = False

        question = input("Do you want to encode(1) or decode(2)? (Choose a number): ")

        if question == "1":

            #encode_base16
            str1 = input("Enter text to encode: ")

            str_a = str1.encode('utf-8')  #convert string to bytes
            base16_bytes = base64.b16encode(str_a)

            print(base16_bytes.decode('utf-8'))
            
        elif question == "2":
            #decode_base16

            str2 = input("Enter text to decode: ")

            str_b = str2.encode('utf-8')  #convert string to bytes
            base16_decoded_bytes = base64.b16decode(str_b)

            print(base16_decoded_bytes.decode('utf-8'))

        else:
            check = True

    elif entry == "2": 
        check = False

        question = input("Do you want to encode(1) or decode(2)? (Choose a number): ")

        if question == "1":

            #encode_base32
            str1 = input("Enter text to encode: ")

            str_a = str1.encode('utf-8')  #convert string to bytes
            base32_bytes = base64.b32encode(str_a)

            print(base32_bytes.decode('utf-8'))
            
        elif question == "2":

            #decode_base32
            str2 = input("Enter text to decode: ")

            str_b = str2.encode('utf-8')  #convert string to bytes
            base32_decoded_bytes = base64.b32decode(str_b)

            print(base32_decoded_bytes.decode('utf-8'))
            
        else:
            check = True

    elif entry == "3":
        check = False

        question = input("Do you want to encode(1) or decode(2)? (Choose a number): ")

        if question == "1":

            #encode_base64
            str1 = input("Enter text to encode: ")

            str_a = str1.encode('utf-8')  #convert string to bytes
            base64_bytes = base64.b64encode(str_a)

            print(base64_bytes.decode('utf-8'))
            
        elif question == "2":

            #decode_base64
            str2 = input("Enter text to decode: ")

            str_b = str2.encode('utf-8')  #convert string to bytes
            base64_decoded_bytes = base64.b64decode(str_b)

            print(base64_decoded_bytes.decode('utf-8'))

        else:
            check = True

    elif entry == "4":
        exit()

    else:
        check = True

