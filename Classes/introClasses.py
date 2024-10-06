'''
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Use yield
'''

class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generate(self):
        """ Generator to yield numbers divisible by 7 from range 0 to n """
        for i in range(self.n+1): # inclusive
            if i%7 == 0:
                yield i

n = int(input("Enter a number (n): "))
div_by_seven = DivisibleBySeven(n)

print(type(div_by_seven.generate()))

# for number in div_by_seven.generate():
#     print(number)

