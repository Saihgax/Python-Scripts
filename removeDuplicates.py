
def removeDuplicate(li):
    new_li = []
    seen = set()

    for item in li:
        if item not in seen:
            seen.add(item)
            new_li.append(item)
    
    return new_li


li=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(li))
