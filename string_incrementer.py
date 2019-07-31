#https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
def increment_string(strng):
    import re
    nb = re.findall(r'\d+',strng)
    if nb:
        new_nb = nb[-1]
        strng = strng.rsplit(new_nb,1)[0]
        nb = str(int(new_nb)+1)
        return strng + '0' * (len(new_nb) - len(nb)) + nb
    return strng + '1'

print(increment_string("foobar001"))
#print(increment_string("bar"))
print(increment_string("foobar99"))
print(increment_string("foobar099"))
