import re

email_address = input("Enter your email address: ")
pattern = "(\w+)@(\w+\.)+(com)"

re_match = re.match(pattern, email_address)
print(re_match.group(1))
