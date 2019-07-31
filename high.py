

x = 'man i need a taxi up to ubud'
y = 'what time are we climbing up the volcano'

def high(x):
    return max(x.split(), key = lambda k: sum(ord(c)-96 for c in k))
#print(high(x))

def high(x):
    words = x.split()
    lst = []
    for i in words:
        scores = sum([ord(char)-96 for char in i])
        print(scores)
        lst.append(scores)
    return words[lst.index(max(lst))]
print (high(x))
