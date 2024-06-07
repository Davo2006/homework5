a = [1,2,3,4,5,6,7]
min_ = a[0]
min = a[0]
for i in a:
    if i<min_:
        min_ = i
for i in a:
    if i<min and i!=min_:
        min = i
print(min)