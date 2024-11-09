import subprocess 

with open("file.txt", 'r') as f:
    lines = f.readlines()
    # print(lines)
    newLines = [line.strip() for line in lines]
    print(newLines)
    
    newList = [word for phrase in newLines for word in phrase.split()]
    '''
    for phrase in newLines:
        for word in phrase.split():
            flattened_list.append(word)
    '''


    print(newList)
#     newItem = []
#     for items in lines:
#         items = items.split()
#         for item in items:
#             newItem.append(item)

# print(newItem)