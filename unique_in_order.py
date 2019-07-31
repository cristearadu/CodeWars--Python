def unique_in_order(iterable):
    lst_final = []
    for ch in iterable:
        if lst_final:
            if lst_final[-1] != ch:
                lst_final.append(ch)
        else:
           lst_final.append(ch)
    return lst_final
print(unique_in_order('AAAABBBCCDAABBB'))

def unique_in_order(iterable):
    result = []
    prev = None
    for ch in iterable:
        if ch != prev:
            result.append(ch)
            prev = ch
    return result
print(unique_in_order('AAAABBBCCDAABBB'))
