import random

# constant variables for code
ASCII_FIRST = ord("A")
ASCII_LAST = ord("Z")
ALPHABET_LENGTH = (ASCII_FIRST - ASCII_LAST) + 1

def Shifter(message, key):
    pass
# placeholder for the encrypted message
    secret_message = ""

        # loop to iterate each character
    for char in message.upper():
            if char.isalpha():
                char_code = ord(char)
                shifted_code = char_code + key

                # in order to ensure code stays alphabetic
                if shifted_code > ASCII_LAST:
                    shifted_code -= ALPHABET_LENGTH
                if shifted_code < ASCII_FIRST:
                    shifted_code += ALPHABET_LENGTH

                # make shifted code back into string
                shift_message = chr(shifted_code)
                secret_message = secret_message + shift_message
            else:
                secret_message = secret_message + char

            # key Randomizer
            if key != 0:
                pass
            else:
                key = random.randint(1, 9)

    print(secret_message)
user_message = input("Enter message to encrypt: ")
user_key = int(input("Enter key: "))
Shifter(user_message, user_key)
