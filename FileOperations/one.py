def count_words(filename):
    try: 
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except Exception as e:
        return "File not found"
    
word_count = count_words('example.txt')
print(word_count)

