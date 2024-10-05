from functools import cmp_to_key

def compare_by_second_element(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] > b[1]:
        return 1
    else:
        return 0


def compare_by_second_element_desc(a, b):
    if a[1] > b[1]:
        return -1
    elif a[1] < b[1]:
        return 1
    else:
        return 0

def compare_by_first_element(a, b):
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    else:
        return 0

data = [(1, 'b'), (2, 'a'), (3, 'c')]

sorted_data = sorted(data, key=cmp_to_key(compare_by_second_element))
print(sorted_data)
# [(2, 'a'), (1, 'b'), (3, 'c')]

sorted_data_desc = sorted(data, key=cmp_to_key(compare_by_second_element_desc))
print(sorted_data_desc)
# [(3, 'c'), (1, 'b'), (2, 'a')]

sorted_data_first = sorted(data, key=cmp_to_key(compare_by_first_element))
print(sorted_data_first)
# [(1, 'b'), (2, 'a'), (3, 'c')]

# OR USING LAMBDA

data2 = [(1, 'b'), (2, 'a'), (3, 'c')]

# Sort by the second element of each tuple using key
sorted_data_lambda = sorted(data2, key=lambda x: x[0])
print(sorted_data_lambda)

