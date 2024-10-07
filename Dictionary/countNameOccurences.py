from collections import Counter
from pprint import pprint

def countNameOccurrences(dicts):
    return Counter(d["name"] for d in dicts)

data = [
    {"name": "John"},
    {"name": "Jane"},
    {"name": "John"},
    {"name": "Doe"}
]

result = countNameOccurrences(data)
pprint(result)




'''
A program which count and 
print the numbers of each character in a string input by console.
'''

s = "abcdefgabc"
dic = {}

for char in s:
    dic[char] = dic.get(char, 0) + 1

print('\t'.join(['%s,%s' %(k, v) for k, v in dic.items()]))

