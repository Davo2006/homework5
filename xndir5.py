a = [1,1,2,3,4,56,7]
b = []
for i in a:
    if not i in a:
        b.append(i)
print(b)