import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    while True: 
        pwd = "" 
        has_number = False
        has_special = False

        while len(pwd) < min_length:
            new_char = random.choice(characters)
            pwd += new_char 
            
            if new_char in digits:
                has_number = True
            elif new_char in special:
                has_special = True

        meets_criteria = True
        if numbers and not has_number:
            meets_criteria = False

        if special_characters and not has_special:
            meets_criteria = False
        
        if meets_criteria:
            return pwd 

#user input
min_length = int(input("enter the minimum length:"))
has_number =input("Do you want to have a numbers (y/n)?").lower() == "y"
has_special =input("Do you want to have special characters (y/n)?").lower() == "y"

#generate and print password
pwd = generate_password(min_length, has_number, has_special)
print("the generated password is :", pwd)