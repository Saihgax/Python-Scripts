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