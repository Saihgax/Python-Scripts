def int_to_string(num):
    if num == 0:
        return "0"
    negative = num < 0
    num = abs(num)

    res = []
    while num > 0:
        digit = num%10
        res.append(chr(digit + ord('0')))
        num //= 10

    if negative:
        res.append("-")
    res = res[::-1]
    
    return ''.join(res)

num = 5
print(type(num))
print(int_to_string(num))
print(type(int_to_string(num)))

