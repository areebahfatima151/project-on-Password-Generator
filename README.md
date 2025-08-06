# project-on-Password-Generator
**Random Password Generator**
This is a simple Python-based Password Generator that creates strong, customizable passwords based on user preferences. It helps you generate secure passwords containing letters, numbers, and special characters, depending on your selected options.

 **Features**
Generate passwords of a user-defined minimum length 

Option to include numbers

Option to include special characters

Ensures all required character types are included

Easy to use via a terminal/command-line interface


**How it works**

The script asks the user for:

Minimum password length

Whether to include numbers

Whether to include special characters


Based on the input:

It builds a character pool using ASCII letters, and optionally digits and punctuation.


It then:

Randomly selects characters from the pool until the minimum length is met.

Ensures at least one digit and/or special character is included if required.

Once a valid password is generated, it is displayed to the user.
The logic is wrapped in a loop to guarantee all user requirements are satisfied before returning the final password.
