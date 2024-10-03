from collections import defaultdict
from pprint import pprint

def group_by_category(dicts):
    grouped = defaultdict(list)
    for d in dicts:
        grouped[d["category"]].append(d)
    return dict(grouped)

data = [
    {"item": "apple", "category": "fruit", "price": 100},
    {"item": "carrot", "category": "vegetable", "price": 10},
    {"item": "banana", "category": "fruit", "price": 209}
]

result = group_by_category(data)
pprint(result)