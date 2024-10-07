
def find_max_score(dicts):
    return max(dicts,key= lambda x: x['score'])

data = [
    {"name": "John", "score": 90},
    {"name": "Jane", "score": 95},
    {"name": "Doe", "score": 85}
]

result = find_max_score(data)
print(result['score'])