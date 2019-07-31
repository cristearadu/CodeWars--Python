def duplicate_encode(word):
    list_chars = []
    for i in word.lower():
        list_chars.append(i)
    set_1 = set(list_chars)
    
    dict_list = {key:0 for key in set_1}
    for key in dict_list.keys():
        for ch in list_chars:
            if ch == key:
                dict_list[key] += 1
                
    str_final=''
    for ch in word.lower():
        if dict_list[ch] > 1:
            str_final += ")"
        else:
            str_final += "("
    return str_final
print(duplicate_encode('CodeWarrior'))

from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    counter = Counter(word)
    return ''.join(('(' if counter[ch] == 1 else ')') for ch in word)


pin = '1234'
if type(int(pin)) != int:
    print ('False')


    
