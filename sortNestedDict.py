# Sort by a key within the nested "details" dictionary.
def sort_by_nested_key(dicts):
    return sorted(dicts, key= lambda x:x["details"]["age"])


data = [
    {"name": "John", "details": {"age": 25}},
    {"name": "Jane", "details": {"age": 30}},
    {"name": "Doe", "details": {"age": 20}}
]

result = sort_by_nested_key(data)
print(result)