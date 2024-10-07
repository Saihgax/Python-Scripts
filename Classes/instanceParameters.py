class Person:
    name = "Person"
    def __init__(self, name=None):
        self.name = name

jeffrey = Person("Jeffrey")
print("%s name is %s" %(Person.name, jeffrey.name))

'''
An instance of Person is created with the name "Jeffrey". This means:

1. The class attribute Person.name is still "Person".
2. The instance attribute jeffrey.name is set to "Jeffrey".
'''

nico = Person()
nico.name = "Nico"
print("%s name is %s" %(Person.name, nico.name))

'''
1. Another instance of Person is created without passing any arguments, so self.name is initially None.
2. The instance attribute nico.name is then explicitly set to "Nico".
'''
