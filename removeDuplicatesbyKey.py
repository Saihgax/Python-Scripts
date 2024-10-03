def remove_dupl_by_id(dicts):
    seen = set()
    unique_list = []

    for d in dicts:
        if d['id'] not in seen:
            unique_list.append(d)
            seen.add(d['id'])
    return unique_list


data = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"},
    {"id": 1, "name": "Doe"}
]

result = remove_dupl_by_id(data)
print(result)
