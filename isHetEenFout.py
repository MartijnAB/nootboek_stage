x = set()
print(x)
x.update(['a','a','b'])
print(x)
x.update(['c', 'b', 'g'])
print(x)

# print(x.__name__)

a = True
b = False

if a and not b:
    print("ja")