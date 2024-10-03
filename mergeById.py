def merge_by_id(list1, list2):
    merged = {d['id']: d for d in list1}
    for d in list2:
        if d['id'] in merged:
            merged[d['id']].update(d) # Combine if id exists
        else:
            merged[d['id']] = d
    return list(merged.values())


list1 = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"}
]

list2 = [
    {"id": 2, "age": 30},
    {"id": 3, "name": "Doe"}
]

result = merge_by_id(list1, list2)
print(result)