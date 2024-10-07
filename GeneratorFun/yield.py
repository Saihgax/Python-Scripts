def evenGenerator(n):
    i = 0
    while i <= n:
        if i%2==0:
            yield i
        i += 1

n = 10
values = []
for i in evenGenerator(n):
    values.append(str(i))

print(','.join(values))