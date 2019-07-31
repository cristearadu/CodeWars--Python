#https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
def increment_string(strng):
    import re
    patt = r"([0-9]+)"
    out = re.search(patt,strng)
    out = out.group()
    print(type(out))
    
    if out:
        index = strng.find(out)
        print(index) 
        pass
    else:
        return strng + "1"
    #return strng

print(increment_string("foobar001"))
#print(increment_string("bar"))
