from collections import Counter

with open('file2.txt', 'r') as file:
    lines = file.readlines()
    
    words = []
    for line in lines:
        for word in line.split():
            words.append(word)

    word_count = Counter(words)

    for word, count in word_count.items():
        print(f"{word} {count}")