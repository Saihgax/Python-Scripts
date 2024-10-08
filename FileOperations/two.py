''' Find and replace text in a file '''

def replace_word_in_file(filename, old_word, new_word):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        content = content.replace(old_word, new_word)
        with open(filename, 'w') as file:
            file.write(content)
        print(f"The word {old_word} has been replaced with {new_word}")
    except FileNotFoundError:
        print("File Not Found.")

replace_word_in_file('example.txt', 'Java', 'Python')
