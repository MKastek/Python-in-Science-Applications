from collections import defaultdict


lst = [1,2,3,4,5]
dict = {'karol':5, 'renata': 9}
print(dict)

print(dict['karol'])
#del kasowanie
print("karol" in dict)

for key in dict:
    print(dict[key])

for key in dict.keys():
    print(key)

for value in dict.values():
    print(value)

for key,value in dict.items():
    print(key,value)

# dict comprehension
x = {i: i * i for i in range(10)}
print(x)

x = defaultdict(int)
#automatycznie zero
print(x['0'])
x['0'] =+ 1
print(x['0'])