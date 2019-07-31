def array_diff(a, b):
    lst = []
    for elem in a:
        if elem not in b:
            lst.append(elem)
    return lst
def array_diff(a,b):
    return list(elem for elem in a if elem not in b)
#print(array_diff([1,2], [1]))
#print(array_diff([1,2,2], [1]))
print(array_diff([1,2,2,3,2,5,4,2,3,3,2], [2]))
