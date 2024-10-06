'''
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. 

The tuples are input by console. 
The sort criteria is: 1: Sort based on name; 2: Then sort based on age; 3: Then sort by score. 
The priority is that name > age > score. 

input: Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 
output: [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''

input_data = [item for item in input("Enter input here: ").split(" ")]

data = []

for item in input_data:
    name, age, score = item.split(",")
    data.append((name, age, score))

# data = [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

sorted_data = sorted(data, key=lambda x: (int(x[1]), x[0], int(x[2])))

for item in sorted_data:
    print(item)