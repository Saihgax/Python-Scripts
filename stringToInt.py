def string_to_int(s):
    result = 0
    negative = False
    start_index = 0

    if s[start_index] == "-":
        negative = True
        start_index += 1
    
    for i in range(start_index, len(s)):
        char = s[i]
        dig = ord(char) - ord('0')

        if 0 <= dig <= 9:
            result = result*10 + dig
        else:
            raise ValueError("Invalid input: Cannot convert to integer.")
        
    return -result if negative else result
    
string_value = "456"

converted_integer = string_to_int(string_value)
print(f"String to integer: {converted_integer} (Type: {type(converted_integer)})")