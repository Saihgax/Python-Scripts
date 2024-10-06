'''
A website requires the users to input username and password to register. Write a program to check the validity of password input by users. Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12 

Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma. 

Example, 
input: ABd1234@1,a F1#,2w3E*,2We3345 
output: ABd1234@1
'''

import re

# Taking input of comma-separated passwords
values = [s for s in input("Enter passwords: ").split(',')]

# List to store valid passwords
valid_passwords = []

# Loop through each password
for p in values:
    # Check the length of the password
    if len(p) < 6 or len(p) > 12:
        continue
    # Check for at least 1 letter between [a-z]
    if not re.search("[a-z]", p):
        continue
    # Check for at least 1 letter between [A-Z]
    if not re.search("[A-Z]", p):
        continue
    # Check for at least 1 number between [0-9]
    if not re.search("[0-9]", p):
        continue
    # Check for at least 1 character from [$#@]
    if not re.search("[$#@]", p):
        continue
    # Check that there is no whitespace
    if re.search("\s", p):
        continue
    
    # If all checks passed, add the password to the valid_passwords list
    valid_passwords.append(p)

# Print the valid passwords, separated by commas
print(",".join(valid_passwords))


