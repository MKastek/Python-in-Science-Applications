lst = []

for i in range(10):
    lst.append(i * i)

print(lst)

lst = [(i, i+1) for i in range(10) if i * i % 2 == 0]
print(lst)


