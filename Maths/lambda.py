'''Using lambda function with filter()'''

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x:x%2!=0, li))
print(final_list)

''' Extract adults from the ages below'''
ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda x: x > 18, ages))
print(adults)

""" lambda fun with map() """

'''Multiply all elements of the list by 2'''
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

result = list(map(lambda x:x*2, li))
print(result)


''' Transform all elements of a list to upper case'''

animals = ['dog', 'cat', 'parrot', 'rabbit']
final_animals = list(map(lambda x: x.upper(), animals))


# for final_animal in final_animals:
print(final_animals)