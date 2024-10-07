def filter_by_price(dicts, threshold):
    return [d for d in dicts if d['price'] >= threshold]

data = [
    {"name": "item1", "price": 10},
    {"name": "item2", "price": 5},
    {"name": "item3", "price": 15}
]

result = filter_by_price(data, 10)
print(result)
